# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class BuildConfigurationSetRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'product_version_id': 'int',
        'build_configuration_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'product_version_id': 'productVersionId',
        'build_configuration_ids': 'buildConfigurationIds'
    }

    def __init__(self, id=None, name=None, product_version_id=None, build_configuration_ids=None):
        """
        BuildConfigurationSetRest - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._product_version_id = None
        self._build_configuration_ids = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if product_version_id is not None:
          self.product_version_id = product_version_id
        if build_configuration_ids is not None:
          self.build_configuration_ids = build_configuration_ids

    @property
    def id(self):
        """
        Gets the id of this BuildConfigurationSetRest.

        :return: The id of this BuildConfigurationSetRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildConfigurationSetRest.

        :param id: The id of this BuildConfigurationSetRest.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuildConfigurationSetRest.

        :return: The name of this BuildConfigurationSetRest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildConfigurationSetRest.

        :param name: The name of this BuildConfigurationSetRest.
        :type: str
        """

        self._name = name

    @property
    def product_version_id(self):
        """
        Gets the product_version_id of this BuildConfigurationSetRest.

        :return: The product_version_id of this BuildConfigurationSetRest.
        :rtype: int
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """
        Sets the product_version_id of this BuildConfigurationSetRest.

        :param product_version_id: The product_version_id of this BuildConfigurationSetRest.
        :type: int
        """

        self._product_version_id = product_version_id

    @property
    def build_configuration_ids(self):
        """
        Gets the build_configuration_ids of this BuildConfigurationSetRest.

        :return: The build_configuration_ids of this BuildConfigurationSetRest.
        :rtype: list[int]
        """
        return self._build_configuration_ids

    @build_configuration_ids.setter
    def build_configuration_ids(self, build_configuration_ids):
        """
        Sets the build_configuration_ids of this BuildConfigurationSetRest.

        :param build_configuration_ids: The build_configuration_ids of this BuildConfigurationSetRest.
        :type: list[int]
        """

        self._build_configuration_ids = build_configuration_ids

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
            elif isinstance(value, datetime):
                result[attr] = str(value.date())
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
        if not isinstance(other, BuildConfigurationSetRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
