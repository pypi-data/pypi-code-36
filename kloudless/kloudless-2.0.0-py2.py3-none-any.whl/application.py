from __future__ import unicode_literals

import base64
import os

import requests

from . import exceptions
from .client import Client
from .util import construct_kloudless_endpoint

try:
    import simplejson as json
except ImportError:
    import json


#  Fix api version to v1 as API documentation described
OAUTH_API_VERSION = 1


def verify_token(app_id, token):
    """
    Verify whether the ``token`` belongs to Application with ``app_id``.

    Refer to `Verify the token <https://developers.kloudless.com/docs/
    latest/authentication#header-verify-the-token>`_  for more information.

    :param str app_id: Application ID
    :param str token: Account's Bearer token

    :return: (dict) Token information
    :raise: :class:`kloudless.exceptions.TokenVerificationFailed`
    """

    client = Client(token=token)
    response = client.get('oauth/token', api_version=OAUTH_API_VERSION)

    data = response.json()
    check_app_id = data['client_id']
    if check_app_id != app_id:
        raise exceptions.TokenVerificationFailed(
            'Token verification failed, the token is grant to {}'
            ' but not {}'.format(check_app_id, app_id)
        )
    return data


def get_authorization_url(
        app_id, redirect_uri, scope='all', state='', extra_data='', **params):
    """
    Get the url to start the first leg of OAuth flow.

    Refer to `Authentication Docs <https://developers.kloudless.com/docs/latest/
    authentication#oauth-2.0>`_ for more information.

    :param str app_id: Application ID

    :param str redirect_uri: Redirect URI to your application server

    :param str scope: A space-delimited string of scopes that indicate which
        services a user can connect, and which permissions to request

    :param str state: An arbitrary string which would be redirected back via
        ``redirect_uri`` as query parameter. Random url-safe Base64 string would
        be generated by default

    :param str extra_data: A URL-encoded JSON object containing data used to
        pre-fill default values for fields in the Kloudless authentication
        forms. For example, the domain of a WebDAV server

    :param params: Additional query parameters

    :returns: `tuple(url, state)`: Redirect the user to ``url`` to start
        authorization. Saved ``state`` in user's session for future validation

    :rtype: `tuple(str, str)`
    """

    if extra_data and isinstance(extra_data, dict):
        extra_data = json.dumps(extra_data)
    if not state:
        state = base64.urlsafe_b64encode(os.urandom(12)).decode('utf8')

    params.update({
        'client_id': app_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope,
        'state': state,
        'extra_data': extra_data,
    })

    endpoint = construct_kloudless_endpoint('oauth',
                                            api_version=OAUTH_API_VERSION)
    url = requests.Request('GET', endpoint, params=params).prepare().url
    return url, state


def get_token_from_code(
        app_id, api_key, orig_state, orig_redirect_uri, **params):
    """
    Retrieve bearer token from authorization code.

    :param str app_id: Application ID

    :param str api_key: API Key

    :param str orig_state: ``state`` from
        :func:`kloudless.application.get_authorization_url` call

    :param str orig_redirect_uri: ``redirect_uri`` used while calling
        :func:`kloudless.application.get_authorization_url`

    :param params: The included query parameters while Kloudless redirects user
        to Redirect URI of your application server

    :return: (str) Bearer token

    :raise: :class:`kloudless.exceptions.OauthFlowFailed`
    """

    if params.get('error'):
        auth_exc = exceptions.OauthFlowFailed(
            "{}: {}".format(params['error'], params['error_description']))
        auth_exc.error_data = params
        raise auth_exc
    if orig_state != params.get('state'):
        raise exceptions.OauthFlowFailed(
            "state values do not match: {} != {}".format(
                orig_state, params.get('state'))
        )
    if not params.get('code'):
        raise exceptions.OauthFlowFailed(
            "An authorization code is required.")

    data = {
        'grant_type': 'authorization_code',
        'code': params['code'],
        'redirect_uri': orig_redirect_uri,
        'client_id': app_id,
        'client_secret': api_key,
    }

    client = Client(api_key=api_key)
    response = client.post(
        'oauth/token', data=data, api_version=OAUTH_API_VERSION,
        headers={'Content-Type': 'application/form-urlencoded'}
    )
    token = response.json()['access_token']
    return token
