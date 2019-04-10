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


class SearchShiftsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, query=None, limit=None, cursor=None):
        """
        SearchShiftsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query': 'ShiftQuery',
            'limit': 'int',
            'cursor': 'str'
        }

        self.attribute_map = {
            'query': 'query',
            'limit': 'limit',
            'cursor': 'cursor'
        }

        self._query = query
        self._limit = limit
        self._cursor = cursor

    @property
    def query(self):
        """
        Gets the query of this SearchShiftsRequest.
        Query filters.

        :return: The query of this SearchShiftsRequest.
        :rtype: ShiftQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchShiftsRequest.
        Query filters.

        :param query: The query of this SearchShiftsRequest.
        :type: ShiftQuery
        """

        self._query = query

    @property
    def limit(self):
        """
        Gets the limit of this SearchShiftsRequest.
        number of resources in a page (200 by default).

        :return: The limit of this SearchShiftsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this SearchShiftsRequest.
        number of resources in a page (200 by default).

        :param limit: The limit of this SearchShiftsRequest.
        :type: int
        """

        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")
        if limit > 200:
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `200`")
        if limit < 1:
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `1`")

        self._limit = limit

    @property
    def cursor(self):
        """
        Gets the cursor of this SearchShiftsRequest.
        opaque cursor for fetching the next page.

        :return: The cursor of this SearchShiftsRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this SearchShiftsRequest.
        opaque cursor for fetching the next page.

        :param cursor: The cursor of this SearchShiftsRequest.
        :type: str
        """

        self._cursor = cursor

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
