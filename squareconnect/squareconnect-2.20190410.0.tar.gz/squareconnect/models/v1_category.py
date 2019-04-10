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


class V1Category(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, v2_id=None):
        """
        V1Category - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'v2_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'v2_id': 'v2_id'
        }

        self._id = id
        self._name = name
        self._v2_id = v2_id

    @property
    def id(self):
        """
        Gets the id of this V1Category.
        The category's unique ID.

        :return: The id of this V1Category.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Category.
        The category's unique ID.

        :param id: The id of this V1Category.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this V1Category.
        The category's name.

        :return: The name of this V1Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Category.
        The category's name.

        :param name: The name of this V1Category.
        :type: str
        """

        self._name = name

    @property
    def v2_id(self):
        """
        Gets the v2_id of this V1Category.
        The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID.

        :return: The v2_id of this V1Category.
        :rtype: str
        """
        return self._v2_id

    @v2_id.setter
    def v2_id(self, v2_id):
        """
        Sets the v2_id of this V1Category.
        The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID.

        :param v2_id: The v2_id of this V1Category.
        :type: str
        """

        self._v2_id = v2_id

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
