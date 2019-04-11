# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RawProperty(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'value': 'str',
        'def_id': 'int'
    }

    attribute_map = {
        'value': 'value',
        'def_id': 'def_id'
    }

    def __init__(self, value=None, def_id=None):  # noqa: E501
        """RawProperty - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._def_id = None
        self.discriminator = None

        self.value = value
        self.def_id = def_id

    @property
    def value(self):
        """Gets the value of this RawProperty.  # noqa: E501


        :return: The value of this RawProperty.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RawProperty.


        :param value: The value of this RawProperty.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def def_id(self):
        """Gets the def_id of this RawProperty.  # noqa: E501


        :return: The def_id of this RawProperty.  # noqa: E501
        :rtype: int
        """
        return self._def_id

    @def_id.setter
    def def_id(self, def_id):
        """Sets the def_id of this RawProperty.


        :param def_id: The def_id of this RawProperty.  # noqa: E501
        :type: int
        """
        if def_id is None:
            raise ValueError("Invalid value for `def_id`, must not be `None`")  # noqa: E501

        self._def_id = def_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RawProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
