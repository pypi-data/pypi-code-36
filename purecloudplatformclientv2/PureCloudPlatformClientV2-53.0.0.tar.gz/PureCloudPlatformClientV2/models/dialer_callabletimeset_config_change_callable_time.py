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


class DialerCallabletimesetConfigChangeCallableTime(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerCallabletimesetConfigChangeCallableTime - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'time_slots': 'list[DialerCallabletimesetConfigChangeTimeSlot]',
            'time_zone_id': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'time_slots': 'timeSlots',
            'time_zone_id': 'timeZoneId',
            'additional_properties': 'additionalProperties'
        }

        self._time_slots = None
        self._time_zone_id = None
        self._additional_properties = None

    @property
    def time_slots(self):
        """
        Gets the time_slots of this DialerCallabletimesetConfigChangeCallableTime.


        :return: The time_slots of this DialerCallabletimesetConfigChangeCallableTime.
        :rtype: list[DialerCallabletimesetConfigChangeTimeSlot]
        """
        return self._time_slots

    @time_slots.setter
    def time_slots(self, time_slots):
        """
        Sets the time_slots of this DialerCallabletimesetConfigChangeCallableTime.


        :param time_slots: The time_slots of this DialerCallabletimesetConfigChangeCallableTime.
        :type: list[DialerCallabletimesetConfigChangeTimeSlot]
        """
        
        self._time_slots = time_slots

    @property
    def time_zone_id(self):
        """
        Gets the time_zone_id of this DialerCallabletimesetConfigChangeCallableTime.


        :return: The time_zone_id of this DialerCallabletimesetConfigChangeCallableTime.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """
        Sets the time_zone_id of this DialerCallabletimesetConfigChangeCallableTime.


        :param time_zone_id: The time_zone_id of this DialerCallabletimesetConfigChangeCallableTime.
        :type: str
        """
        
        self._time_zone_id = time_zone_id

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DialerCallabletimesetConfigChangeCallableTime.


        :return: The additional_properties of this DialerCallabletimesetConfigChangeCallableTime.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DialerCallabletimesetConfigChangeCallableTime.


        :param additional_properties: The additional_properties of this DialerCallabletimesetConfigChangeCallableTime.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

