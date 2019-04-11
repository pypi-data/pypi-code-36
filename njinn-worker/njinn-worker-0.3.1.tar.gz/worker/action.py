import configparser
import importlib
import io
import json
import os
import signal
import sys
from contextlib import redirect_stderr, redirect_stdout
import re

import requests
from cryptography.fernet import Fernet, InvalidToken
from requests_jwt import JWTAuth, payload_path


class Task():

    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.log = None
        self.preperation_log = io.StringIO()
        self.result = dict()
        self.state_info = ""

    def read_input_file(self):
        # load parameters
        with open(self.input_file_path) as input_file:
            self.input = json.load(input_file)

        self.working_dir = os.path.dirname(
            os.path.abspath(self.input_file_path))

        self.action = self.input["action"]
        self.pack = self.input["pack"]
        self.config_path = self.input["config_path"]

    def load_action(self):
        # import action (try)
        action_entry_point = self.action.split(':')
        action_module = action_entry_point[0]
        action_class_name = action_entry_point[1]

        module = f"packs.{self.pack}.{action_module}"
        mod = importlib.import_module(module)
        action_class = getattr(mod, action_class_name)
        
        print(f"Running Action: {self.pack}.{action_class_name} ({self.pack}.{self.action})", file=self.preperation_log)
        self.action = action_class()

    def set_njinn_api(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)

        njinn_api = config['DEFAULT']['njinn_api']
        secret = config['DEFAULT']['secret']
        worker_name = config['DEFAULT']['name']
        self.secrets_key = config['DEFAULT']['secrets_key']

        njinn = NjinnAPI(njinn_api, secret, worker_name)
        setattr(self.action, '_njinn', njinn)


    def decrypt_secret_value(self, value, pattern=r'SECRET\((\S*)\)'):
        """
        Looks for an encrypted variable and decrypt if found and
        also replaces it with the decrypted variable in ``value``.
        """

        original_value = value
        secret_values = re.findall(pattern, value)
        if secret_values:
            for secret_value in secret_values:
                f = Fernet(self.secrets_key)
                encrypted_variable = secret_value.encode()

                try:
                    variable = f.decrypt(encrypted_variable).decode()
                    value = re.sub(pattern, variable, value, count=1)
                except InvalidToken:
                    print("Invalid token for decryption of secret values.", file=self.preperation_log)

            value_log = re.sub(pattern, '*' * 6, original_value)
        else:
            value_log = original_value

        return value, value_log


    def set_action_parameters(self):
        params = self.input['action_context']['parameters']

        for param, value in params.items():
            value, value_log = self.decrypt_secret_value(value)

            print(f"Setting \"{param}\" to \"{value_log}\"", file=self.preperation_log)
            setattr(self.action, param, value)

        print("", file=self.preperation_log)

    def write_output_file(self):
        # writes self.stdout, self.stderr, self.run_return, ... to output file
        self.result['output'] = self.output
        self.result['log'] = self.preperation_log.getvalue() + self.log + f"\n{self.state.capitalize()}"
        self.result['state'] = self.state
        self.result['state_info'] = self.state_info

        with open(os.path.join(self.working_dir, 'out.json'), 'w') as fp:
            json.dump(self.result, fp)

    def setup_signals(self):
        """
        Sets up handler to process signals from the OS.
        """

        def signal_handler(signum, frame):
            """Setting kill signal handler"""
            # self.log.error("Killing subprocess")
            self.action.on_kill()
            raise Exception("Task received SIGTERM signal")

        signal.signal(signal.SIGTERM, signal_handler)

    def run_action(self):

        self.output = None
        self.log = ""

        try:
            self.read_input_file()
            self.load_action()
            self.set_njinn_api()
            self.set_action_parameters()
            self.setup_signals()

            # setup logger to catch stdout/stderr to write to output file
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                with redirect_stderr(stdout):
                    action_return = self.action.run()

            self.log = stdout.getvalue()

            if action_return is not None:
                if isinstance(action_return, dict):
                    self.output = action_return
                else:
                    self.output = {'result': action_return}

            self.state = "SUCCESS"

        except (Exception, KeyboardInterrupt) as e:
            self.state_info = str(e)
            self.output = {"error": self.state_info}
            self.state = "ERROR"
            self.log += self.state_info

        finally:
            self.write_output_file()


class NjinnAPI():
    """
    Class provides access to the Njinn API by adding the
    base URL and authentication (JWT) to each request.
    """

    def __init__(self, api, token, worker_name):
        """
        Prepare Njinn base URL and token for authentication
        """

        self.auth = JWTAuth(token)
        self.auth.expire(30)
        self.auth.add_field('worker', worker_name)
        self.auth.add_field('path', payload_path)

        self.njinn_api = api

    def get_url(self, path):
        """
        Add the Njinn API base url infront of the path.
        """

        path = path[1:] if path.startswith('/') else path
        url = f"{self.njinn_api}/{path}"
        return url

    def get(self, path, params=None, **kwargs):
        """
        Run GET request to the Njinn API.
        """

        url = self.get_url(path)
        return requests.get(url, params=params, auth=self.auth, **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        """
        Run POST request to the Njinn API.
        """

        url = self.get_url(path)
        return requests.post(url, data=data, json=json, auth=self.auth, **kwargs)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Invalid call. Require exactly one argument, which is the path to the inputfile.")
        sys.exit(1)

    task = Task(sys.argv[1])
    task.run_action()
