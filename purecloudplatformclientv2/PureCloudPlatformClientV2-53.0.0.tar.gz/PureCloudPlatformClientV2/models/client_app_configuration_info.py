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


class ClientAppConfigurationInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClientAppConfigurationInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current': 'IntegrationConfiguration',
            'effective': 'EffectiveConfiguration'
        }

        self.attribute_map = {
            'current': 'current',
            'effective': 'effective'
        }

        self._current = None
        self._effective = None

    @property
    def current(self):
        """
        Gets the current of this ClientAppConfigurationInfo.
        The current, active configuration for the integration.

        :return: The current of this ClientAppConfigurationInfo.
        :rtype: IntegrationConfiguration
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this ClientAppConfigurationInfo.
        The current, active configuration for the integration.

        :param current: The current of this ClientAppConfigurationInfo.
        :type: IntegrationConfiguration
        """
        
        self._current = current

    @property
    def effective(self):
        """
        Gets the effective of this ClientAppConfigurationInfo.
        The effective configuration for the app, containing the integration specific configuration along with overrides specified in the integration type.

        :return: The effective of this ClientAppConfigurationInfo.
        :rtype: EffectiveConfiguration
        """
        return self._effective

    @effective.setter
    def effective(self, effective):
        """
        Sets the effective of this ClientAppConfigurationInfo.
        The effective configuration for the app, containing the integration specific configuration along with overrides specified in the integration type.

        :param effective: The effective of this ClientAppConfigurationInfo.
        :type: EffectiveConfiguration
        """
        
        self._effective = effective

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

