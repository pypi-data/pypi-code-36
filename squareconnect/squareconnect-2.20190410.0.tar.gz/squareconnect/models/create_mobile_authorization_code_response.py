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


class CreateMobileAuthorizationCodeResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, authorization_code=None, expires_at=None, error=None):
        """
        CreateMobileAuthorizationCodeResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'authorization_code': 'str',
            'expires_at': 'str',
            'error': 'Error'
        }

        self.attribute_map = {
            'authorization_code': 'authorization_code',
            'expires_at': 'expires_at',
            'error': 'error'
        }

        self._authorization_code = authorization_code
        self._expires_at = expires_at
        self._error = error

    @property
    def authorization_code(self):
        """
        Gets the authorization_code of this CreateMobileAuthorizationCodeResponse.
        Generated authorization code that connects a mobile application instance to a Square account.

        :return: The authorization_code of this CreateMobileAuthorizationCodeResponse.
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """
        Sets the authorization_code of this CreateMobileAuthorizationCodeResponse.
        Generated authorization code that connects a mobile application instance to a Square account.

        :param authorization_code: The authorization_code of this CreateMobileAuthorizationCodeResponse.
        :type: str
        """

        self._authorization_code = authorization_code

    @property
    def expires_at(self):
        """
        Gets the expires_at of this CreateMobileAuthorizationCodeResponse.
        The timestamp when `authorization_code` expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, e.g., \"2016-09-04T23:59:33.123Z\".

        :return: The expires_at of this CreateMobileAuthorizationCodeResponse.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """
        Sets the expires_at of this CreateMobileAuthorizationCodeResponse.
        The timestamp when `authorization_code` expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, e.g., \"2016-09-04T23:59:33.123Z\".

        :param expires_at: The expires_at of this CreateMobileAuthorizationCodeResponse.
        :type: str
        """

        self._expires_at = expires_at

    @property
    def error(self):
        """
        Gets the error of this CreateMobileAuthorizationCodeResponse.
        An error object that provides details about how creation of authorization code failed.

        :return: The error of this CreateMobileAuthorizationCodeResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this CreateMobileAuthorizationCodeResponse.
        An error object that provides details about how creation of authorization code failed.

        :param error: The error of this CreateMobileAuthorizationCodeResponse.
        :type: Error
        """

        self._error = error

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
