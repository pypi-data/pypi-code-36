# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AdditionalServiceResponse(object):
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
        'configurations': 'list[Configuration]',
        'definition': 'BasicDefinitionResponse',
        'description': 'str'
    }

    attribute_map = {
        'configurations': 'configurations',
        'definition': 'definition',
        'description': 'description'
    }

    def __init__(self, configurations=None, definition=None, description=None):  # noqa: E501
        """AdditionalServiceResponse - a model defined in OpenAPI"""  # noqa: E501

        self._configurations = None
        self._definition = None
        self._description = None
        self.discriminator = None

        if configurations is not None:
            self.configurations = configurations
        if definition is not None:
            self.definition = definition
        if description is not None:
            self.description = description

    @property
    def configurations(self):
        """Gets the configurations of this AdditionalServiceResponse.  # noqa: E501


        :return: The configurations of this AdditionalServiceResponse.  # noqa: E501
        :rtype: list[Configuration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this AdditionalServiceResponse.


        :param configurations: The configurations of this AdditionalServiceResponse.  # noqa: E501
        :type: list[Configuration]
        """

        self._configurations = configurations

    @property
    def definition(self):
        """Gets the definition of this AdditionalServiceResponse.  # noqa: E501


        :return: The definition of this AdditionalServiceResponse.  # noqa: E501
        :rtype: BasicDefinitionResponse
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this AdditionalServiceResponse.


        :param definition: The definition of this AdditionalServiceResponse.  # noqa: E501
        :type: BasicDefinitionResponse
        """

        self._definition = definition

    @property
    def description(self):
        """Gets the description of this AdditionalServiceResponse.  # noqa: E501


        :return: The description of this AdditionalServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdditionalServiceResponse.


        :param description: The description of this AdditionalServiceResponse.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, AdditionalServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
