# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class ObtainTokenRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, client_id=None, client_secret=None, code=None, redirect_uri=None, grant_type=None, refresh_token=None, migration_token=None):
        """
        ObtainTokenRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_id': 'str',
            'client_secret': 'str',
            'code': 'str',
            'redirect_uri': 'str',
            'grant_type': 'str',
            'refresh_token': 'str',
            'migration_token': 'str'
        }

        self.attribute_map = {
            'client_id': 'client_id',
            'client_secret': 'client_secret',
            'code': 'code',
            'redirect_uri': 'redirect_uri',
            'grant_type': 'grant_type',
            'refresh_token': 'refresh_token',
            'migration_token': 'migration_token'
        }

        self._client_id = client_id
        self._client_secret = client_secret
        self._code = code
        self._redirect_uri = redirect_uri
        self._grant_type = grant_type
        self._refresh_token = refresh_token
        self._migration_token = migration_token

    @property
    def client_id(self):
        """
        Gets the client_id of this ObtainTokenRequest.
        The Square-issued ID of your application, available from the [application dashboard](https://connect.squareup.com/apps).

        :return: The client_id of this ObtainTokenRequest.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this ObtainTokenRequest.
        The Square-issued ID of your application, available from the [application dashboard](https://connect.squareup.com/apps).

        :param client_id: The client_id of this ObtainTokenRequest.
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this ObtainTokenRequest.
        The Square-issued application secret for your application, available from the [application dashboard](https://connect.squareup.com/apps).

        :return: The client_secret of this ObtainTokenRequest.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this ObtainTokenRequest.
        The Square-issued application secret for your application, available from the [application dashboard](https://connect.squareup.com/apps).

        :param client_secret: The client_secret of this ObtainTokenRequest.
        :type: str
        """

        self._client_secret = client_secret

    @property
    def code(self):
        """
        Gets the code of this ObtainTokenRequest.
        The authorization code to exchange. This is required if `grant_type` is set to `authorization_code`, to indicate that the application wants to exchange an authorization code for an OAuth access token.

        :return: The code of this ObtainTokenRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ObtainTokenRequest.
        The authorization code to exchange. This is required if `grant_type` is set to `authorization_code`, to indicate that the application wants to exchange an authorization code for an OAuth access token.

        :param code: The code of this ObtainTokenRequest.
        :type: str
        """

        self._code = code

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this ObtainTokenRequest.
        The redirect URL assigned in the [application dashboard](https://connect.squareup.com/apps).

        :return: The redirect_uri of this ObtainTokenRequest.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this ObtainTokenRequest.
        The redirect URL assigned in the [application dashboard](https://connect.squareup.com/apps).

        :param redirect_uri: The redirect_uri of this ObtainTokenRequest.
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def grant_type(self):
        """
        Gets the grant_type of this ObtainTokenRequest.
        Specifies the method to request an OAuth access token. Valid values are: `authorization_code`, `refresh_token`, and `migration_token`

        :return: The grant_type of this ObtainTokenRequest.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """
        Sets the grant_type of this ObtainTokenRequest.
        Specifies the method to request an OAuth access token. Valid values are: `authorization_code`, `refresh_token`, and `migration_token`

        :param grant_type: The grant_type of this ObtainTokenRequest.
        :type: str
        """

        self._grant_type = grant_type

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this ObtainTokenRequest.
        A valid refresh token for generating a new OAuth access token. A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.

        :return: The refresh_token of this ObtainTokenRequest.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this ObtainTokenRequest.
        A valid refresh token for generating a new OAuth access token. A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.

        :param refresh_token: The refresh_token of this ObtainTokenRequest.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def migration_token(self):
        """
        Gets the migration_token of this ObtainTokenRequest.
        Legacy OAuth access token obtained using a Connect API version prior to 2019-03-13. This parameter is required if `grant_type` is set to `migration_token` to indicate that the application wants to get a replacement OAuth access token. The response also returns a refresh token. For more information, see [Migrate to Using Refresh Tokens](/authz/oauth/migration).

        :return: The migration_token of this ObtainTokenRequest.
        :rtype: str
        """
        return self._migration_token

    @migration_token.setter
    def migration_token(self, migration_token):
        """
        Sets the migration_token of this ObtainTokenRequest.
        Legacy OAuth access token obtained using a Connect API version prior to 2019-03-13. This parameter is required if `grant_type` is set to `migration_token` to indicate that the application wants to get a replacement OAuth access token. The response also returns a refresh token. For more information, see [Migrate to Using Refresh Tokens](/authz/oauth/migration).

        :param migration_token: The migration_token of this ObtainTokenRequest.
        :type: str
        """

        self._migration_token = migration_token

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
