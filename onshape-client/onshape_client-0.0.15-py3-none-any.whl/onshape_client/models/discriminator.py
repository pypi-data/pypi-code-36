# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.96
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Discriminator(object):
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
        'property_name': 'str',
        'mapping': 'dict(str, str)'
    }

    attribute_map = {
        'property_name': 'propertyName',
        'mapping': 'mapping'
    }

    def __init__(self, property_name=None, mapping=None):  # noqa: E501
        """Discriminator - a model defined in OpenAPI"""  # noqa: E501

        self._property_name = None
        self._mapping = None
        self.discriminator = None

        if property_name is not None:
            self.property_name = property_name
        if mapping is not None:
            self.mapping = mapping

    @property
    def property_name(self):
        """Gets the property_name of this Discriminator.  # noqa: E501


        :return: The property_name of this Discriminator.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this Discriminator.


        :param property_name: The property_name of this Discriminator.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    @property
    def mapping(self):
        """Gets the mapping of this Discriminator.  # noqa: E501


        :return: The mapping of this Discriminator.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this Discriminator.


        :param mapping: The mapping of this Discriminator.  # noqa: E501
        :type: dict(str, str)
        """

        self._mapping = mapping

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
        if not isinstance(other, Discriminator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
