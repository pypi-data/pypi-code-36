# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ChangeMyPasswordRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ChangeMyPasswordRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'new_password': 'str',
            'old_password': 'str'
        }

        self.attribute_map = {
            'new_password': 'newPassword',
            'old_password': 'oldPassword'
        }

        self._new_password = None
        self._old_password = None

    @property
    def new_password(self):
        """
        Gets the new_password of this ChangeMyPasswordRequest.
        The new password

        :return: The new_password of this ChangeMyPasswordRequest.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """
        Sets the new_password of this ChangeMyPasswordRequest.
        The new password

        :param new_password: The new_password of this ChangeMyPasswordRequest.
        :type: str
        """
        
        self._new_password = new_password

    @property
    def old_password(self):
        """
        Gets the old_password of this ChangeMyPasswordRequest.
        Your current password

        :return: The old_password of this ChangeMyPasswordRequest.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """
        Sets the old_password of this ChangeMyPasswordRequest.
        Your current password

        :param old_password: The old_password of this ChangeMyPasswordRequest.
        :type: str
        """
        
        self._old_password = old_password

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

