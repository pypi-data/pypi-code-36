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


class BreakType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, location_id=None, break_name=None, expected_duration=None, is_paid=None, version=None, created_at=None, updated_at=None):
        """
        BreakType - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'location_id': 'str',
            'break_name': 'str',
            'expected_duration': 'str',
            'is_paid': 'bool',
            'version': 'int',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'location_id': 'location_id',
            'break_name': 'break_name',
            'expected_duration': 'expected_duration',
            'is_paid': 'is_paid',
            'version': 'version',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._location_id = location_id
        self._break_name = break_name
        self._expected_duration = expected_duration
        self._is_paid = is_paid
        self._version = version
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this BreakType.
        UUID for this object.

        :return: The id of this BreakType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BreakType.
        UUID for this object.

        :param id: The id of this BreakType.
        :type: str
        """

        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than `255`")

        self._id = id

    @property
    def location_id(self):
        """
        Gets the location_id of this BreakType.
        The ID of the business location this type of break applies to.

        :return: The location_id of this BreakType.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this BreakType.
        The ID of the business location this type of break applies to.

        :param location_id: The location_id of this BreakType.
        :type: str
        """

        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")
        if len(location_id) < 1:
            raise ValueError("Invalid value for `location_id`, length must be greater than or equal to `1`")

        self._location_id = location_id

    @property
    def break_name(self):
        """
        Gets the break_name of this BreakType.
        A human-readable name for this type of break. Will be displayed to employees in Square products.

        :return: The break_name of this BreakType.
        :rtype: str
        """
        return self._break_name

    @break_name.setter
    def break_name(self, break_name):
        """
        Sets the break_name of this BreakType.
        A human-readable name for this type of break. Will be displayed to employees in Square products.

        :param break_name: The break_name of this BreakType.
        :type: str
        """

        if break_name is None:
            raise ValueError("Invalid value for `break_name`, must not be `None`")
        if len(break_name) < 1:
            raise ValueError("Invalid value for `break_name`, length must be greater than or equal to `1`")

        self._break_name = break_name

    @property
    def expected_duration(self):
        """
        Gets the expected_duration of this BreakType.
        Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of this break. Precision below minutes is truncated.

        :return: The expected_duration of this BreakType.
        :rtype: str
        """
        return self._expected_duration

    @expected_duration.setter
    def expected_duration(self, expected_duration):
        """
        Sets the expected_duration of this BreakType.
        Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of this break. Precision below minutes is truncated.

        :param expected_duration: The expected_duration of this BreakType.
        :type: str
        """

        if expected_duration is None:
            raise ValueError("Invalid value for `expected_duration`, must not be `None`")
        if len(expected_duration) < 1:
            raise ValueError("Invalid value for `expected_duration`, length must be greater than or equal to `1`")

        self._expected_duration = expected_duration

    @property
    def is_paid(self):
        """
        Gets the is_paid of this BreakType.
        Whether this break counts towards time worked for compensation purposes.

        :return: The is_paid of this BreakType.
        :rtype: bool
        """
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        """
        Sets the is_paid of this BreakType.
        Whether this break counts towards time worked for compensation purposes.

        :param is_paid: The is_paid of this BreakType.
        :type: bool
        """

        self._is_paid = is_paid

    @property
    def version(self):
        """
        Gets the version of this BreakType.
        Used for resolving concurrency issues; request will fail if version provided does not match server version at time of request. If a value is not provided, Square's servers execute a \"blind\" write; potentially  overwriting another writer's data.

        :return: The version of this BreakType.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this BreakType.
        Used for resolving concurrency issues; request will fail if version provided does not match server version at time of request. If a value is not provided, Square's servers execute a \"blind\" write; potentially  overwriting another writer's data.

        :param version: The version of this BreakType.
        :type: int
        """

        self._version = version

    @property
    def created_at(self):
        """
        Gets the created_at of this BreakType.
        A read-only timestamp in RFC 3339 format.

        :return: The created_at of this BreakType.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this BreakType.
        A read-only timestamp in RFC 3339 format.

        :param created_at: The created_at of this BreakType.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this BreakType.
        A read-only timestamp in RFC 3339 format.

        :return: The updated_at of this BreakType.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this BreakType.
        A read-only timestamp in RFC 3339 format.

        :param updated_at: The updated_at of this BreakType.
        :type: str
        """

        self._updated_at = updated_at

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
