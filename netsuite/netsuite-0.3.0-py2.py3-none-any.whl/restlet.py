import json
import logging
from typing import Any

import requests
import requests_oauthlib

from . import util

logger = logging.getLogger(__name__)


class NetsuiteRestlet:

    _restlet_path_tmpl = \
        '/app/site/hosting/restlet.nl?script={script_id}&deploy={deploy}'

    def __init__(self, config, *, hostname=None):
        self.__config = config
        self.__hostname = hostname or self._make_default_hostname()

    @property
    def config(self):
        return self.__config

    @property
    def hostname(self):
        return self.__hostname

    def request(
        self,
        script_id: int,
        payload: Any = None,
        *,
        deploy: int = 1,
        raise_on_bad_status: bool = True,
    ):
        raw_request = self.raw_request(
            script_id=script_id,
            payload=payload,
            deploy=deploy,
            raise_on_bad_status=raise_on_bad_status,
        )
        return raw_request.json()

    def raw_request(
        self,
        script_id: int,
        payload: Any = None,
        *,
        deploy: int = 1,
        raise_on_bad_status: bool = True,
    ):
        url = self._make_url(script_id=script_id, deploy=deploy)
        auth = self._make_auth()
        headers = self._make_headers()

        req_headers_json = json.dumps(headers)
        logger.debug(
            f'Making request to restlet at {url}. Payload {payload}. '
            f'Headers: {req_headers_json}'
        )

        resp = requests.post(url, headers=headers, auth=auth, json=payload)

        resp_headers_json = json.dumps(dict(resp.headers))
        logger.debug(f'Got response headers: {resp_headers_json}')

        util.raise_for_status_with_body(resp)
        return resp

    def _make_default_hostname(self):
        account_slugified = self.config.account.lower().replace('_', '-')
        return f'{account_slugified}.restlets.api.netsuite.com'

    def _make_restlet_path(self, script_id: int, deploy: int = 1):
        return self._restlet_path_tmpl.format(
            script_id=script_id,
            deploy=deploy,
        )

    def _make_url(self, script_id: int, deploy: int = 1):
        path = self._make_restlet_path(script_id=script_id, deploy=deploy)
        return f'https://{self.hostname}{path}'

    def _make_auth(self):
        return requests_oauthlib.OAuth1(
            client_key=self.config.consumer_key,
            client_secret=self.config.consumer_secret,
            resource_owner_key=self.config.token_id,
            resource_owner_secret=self.config.token_secret,
            realm=self.config.account,
        )

    def _make_headers(self):
        return {
            'Content-Type': 'application/json',
        }
