import getpass
import logging
import os
import sys
import tempfile

import click
import click_log
import click_spinner
import git
import requests
import tldextract
import yaml

logger = logging.getLogger(__name__)


def login(username, password, base_api):
    auth_url = base_api + '/api/token/auth'

    credentials = {
        "username": username,
        "password": password
    }

    auth_response = requests.post(auth_url, json=credentials)

    if not auth_response.ok:
        raise click.ClickException("Wrong credentials")
    
    jwt_token = auth_response.json()['token']

    headers = {
        "Authorization": f"JWT {jwt_token}"
    }

    global r
    r = requests.Session()
    r.headers.update(headers)


def prepare_actions(config):
    actions_data = []
    actions = config['actions']

    for (key, value) in actions.items():
        action = {
            "name": key,
            "title": value.get('title'),
            "description": value.get('description', ""),
            "icon": value.get('icon', ""),
            "path": value.get('path'),
            "parameters": value.get('parameters', {}),
            "output": value.get('output', {})
        }
        actions_data.append(action)

    logger.info(f"Obtained actions: {len(actions_data)}")
    
    return actions_data


def prepare_config_schemes(config):
    config_schemes_data = []
    config_schemes= config.get('config-schemes', {})

    if config_schemes:
        for (key, _) in config_schemes.items():
            config_scheme = {
                "name": key,
                "input_scheme": config_schemes[key]
            }
            config_schemes_data.append(config_scheme)

    logger.info(f"Obtained config schemes: {len(config_schemes_data)}")

    return config_schemes_data


def prepare_pack(config, repository, branch):
    pack_data = {
        "name": config.get('name'),
        "title": config.get('title'),
        "description": config.get('description', ""),
        "repository": repository,
        "branch": branch
    }

    return pack_data


def create_or_update(endpoint, data, full_name):
    """
    Creates or updates Pack or Action or ConfigScheme object.
    Depends on the 'endpoint' argument.

    If the 'endpoint' is different than for Pack model,
    the 'pack_full_name' argument is mandatory.
    """

    model = endpoint.split("/")[-1][:-1]

    get_obj_url = endpoint + f"?full_name={full_name}"
    obj_response = r.get(get_obj_url)

    if (obj_response.status_code // 100) != 2:
        raise click.ClickException("Could not create or update. API status code: %s, data: %s" %
                                   (obj_response.status_code, obj_response.text))

    count = obj_response.json()['count']

    response = {}

    if count == 0:
        logger.info(f"Creating the {model}")
        response = r.post(endpoint, json=data)
    elif count == 1:
        obj_id = obj_response.json()['results'][0]['id']
        obj_name = data['title'] if data.get('title') else data['name']
        obj_url = endpoint + f"/{obj_id}"

        logger.info(f"Updating the {model}: {obj_name}")
        response = r.put(obj_url, json=data)
    else:
        logger.error(f"{obj_response.json()}")
        raise click.ClickException("Fatal error. More than one object with these values. \
                                    Please contact with our support.")

    if (response.status_code // 100) != 2:
        raise click.ClickException("Could not create or update. API status code: %s, data: %s" %
                                   (response.status_code, response.text))

    return response.json()


def clone_repository(repository_url, path, branch):
    """
    Clone Git repository from "repository_url" into the "path"
    from the "branch" branch.
    """

    logger.info("Cloning repository from %s to the %s" % 
                    (repository_url, path))

    git.Repo.clone_from(repository_url, path, branch=branch)


def get_namespace(url):
    """
    Returns the namespace of the user based on API url.
    """

    parsed_url = tldextract.extract(url)
    namespace = parsed_url.subdomain

    if namespace in ['api', '']:
        return 'njinn'
    return namespace


def check_api(api):
    """
    Checks if 'NJINN_URL' environment variable was overwritten via CLI argument
    or if it was set; returns it, otherwise displays prompt to provide value.
    """

    if not api:
        api = os.environ.get("NJINN_URL")
        if not api:
            api = input("API url: ")

    return api


def check_username(username):
    """
    Checks if 'NJINN_USER' environment variable was overwritten via CLI argument
    or if it was set; returns it, otherwise displays prompt to provide value.
    """

    if not username:
        username = os.environ.get("NJINN_USER")
        if not username:
            username = input("Username: ")

    return username


def check_password(password):
    """
    Checks if 'NJINN_PASS' environment variable was overwritten via CLI argument
    or if it was set; returns it, otherwise displays prompt to provide value.
    """

    if not password:
        password = os.environ.get("NJINN_PASS")
        if not password:
            password = getpass.getpass()

    return password


def install(repository_url, branch, username, password, api):
    os.environ["GIT_TERMINAL_PROMPT"] = "0"

    api = check_api(api)
    username = check_username(username)
    logger.info(f"Login user: {username} @ {api}")
    password = check_password(password)

    login(username, password, api)

    with tempfile.TemporaryDirectory() as temp_dir:

        clone_repository(repository_url, temp_dir, branch=branch)

        pack_conf_name = "pack.yaml" if os.path.exists(f"{temp_dir}/pack.yaml") else "pack.yml"
        pack_conf_path = os.path.join(temp_dir, pack_conf_name)

        if not os.path.exists(pack_conf_path):
            raise click.ClickException("No configuration file in the repository root.")

        try:
            with open(pack_conf_path, 'r') as pack_conf:
                logger.info("Loading the configuration file: %s" % pack_conf_name)
                config = yaml.load(pack_conf, Loader=yaml.FullLoader)

                pack_data = prepare_pack(config, repository_url, branch)
                config_schemes_data = prepare_config_schemes(config)
                actions_data = prepare_actions(config)

                base_api = api + '/api/v1'
                namespace = get_namespace(base_api)
                
                pack_full_name = ".".join([namespace, pack_data['name']]) 
                packs_url = base_api + '/packs'
                pack = create_or_update(packs_url, pack_data, pack_full_name)

                pack_id = pack['id']
                pack_url = pack['url']

                if config_schemes_data:
                    config_schemes_url = base_api + '/config_schemes'
                    for config_scheme in config_schemes_data:
                        config_full_name = ".".join([pack_full_name, config_scheme['name']]) 
                        config_scheme["pack"] = pack_url
                        create_or_update(config_schemes_url, config_scheme, config_full_name)

                actions_url = base_api + '/actions'
                for action in actions_data:
                    action_full_name = ".".join([pack_full_name, action['name']])
                    action["pack_id"] = pack_id
                    create_or_update(actions_url, action, action_full_name)

        except OSError as e:
            raise click.ClickException("Could not open the file. %s" % str(e))
        except KeyError as e:
            raise click.ClickException("Invalid configured %s file. %s" % (pack_conf_name, e))

    logger.info("Installation was successful")
