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


class ProductRest(object):
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
        'description': 'str',
        'abbreviation': 'str',
        'product_code': 'str',
        'pgm_system_name': 'str',
        'product_version_ids': 'list[int]',
        'product_version_refs': 'list[ProductVersionRefRest]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'abbreviation': 'abbreviation',
        'product_code': 'productCode',
        'pgm_system_name': 'pgmSystemName',
        'product_version_ids': 'productVersionIds',
        'product_version_refs': 'productVersionRefs'
    }

    def __init__(self, id=None, name=None, description=None, abbreviation=None, product_code=None, pgm_system_name=None, product_version_ids=None, product_version_refs=None):
        """
        ProductRest - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._abbreviation = None
        self._product_code = None
        self._pgm_system_name = None
        self._product_version_ids = None
        self._product_version_refs = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if abbreviation is not None:
          self.abbreviation = abbreviation
        if product_code is not None:
          self.product_code = product_code
        if pgm_system_name is not None:
          self.pgm_system_name = pgm_system_name
        if product_version_ids is not None:
          self.product_version_ids = product_version_ids
        if product_version_refs is not None:
          self.product_version_refs = product_version_refs

    @property
    def id(self):
        """
        Gets the id of this ProductRest.

        :return: The id of this ProductRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductRest.

        :param id: The id of this ProductRest.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ProductRest.

        :return: The name of this ProductRest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductRest.

        :param name: The name of this ProductRest.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ProductRest.

        :return: The description of this ProductRest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProductRest.

        :param description: The description of this ProductRest.
        :type: str
        """

        self._description = description

    @property
    def abbreviation(self):
        """
        Gets the abbreviation of this ProductRest.

        :return: The abbreviation of this ProductRest.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """
        Sets the abbreviation of this ProductRest.

        :param abbreviation: The abbreviation of this ProductRest.
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def product_code(self):
        """
        Gets the product_code of this ProductRest.

        :return: The product_code of this ProductRest.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """
        Sets the product_code of this ProductRest.

        :param product_code: The product_code of this ProductRest.
        :type: str
        """

        self._product_code = product_code

    @property
    def pgm_system_name(self):
        """
        Gets the pgm_system_name of this ProductRest.

        :return: The pgm_system_name of this ProductRest.
        :rtype: str
        """
        return self._pgm_system_name

    @pgm_system_name.setter
    def pgm_system_name(self, pgm_system_name):
        """
        Sets the pgm_system_name of this ProductRest.

        :param pgm_system_name: The pgm_system_name of this ProductRest.
        :type: str
        """

        self._pgm_system_name = pgm_system_name

    @property
    def product_version_ids(self):
        """
        Gets the product_version_ids of this ProductRest.

        :return: The product_version_ids of this ProductRest.
        :rtype: list[int]
        """
        return self._product_version_ids

    @product_version_ids.setter
    def product_version_ids(self, product_version_ids):
        """
        Sets the product_version_ids of this ProductRest.

        :param product_version_ids: The product_version_ids of this ProductRest.
        :type: list[int]
        """

        self._product_version_ids = product_version_ids

    @property
    def product_version_refs(self):
        """
        Gets the product_version_refs of this ProductRest.

        :return: The product_version_refs of this ProductRest.
        :rtype: list[ProductVersionRefRest]
        """
        return self._product_version_refs

    @product_version_refs.setter
    def product_version_refs(self, product_version_refs):
        """
        Sets the product_version_refs of this ProductRest.

        :param product_version_refs: The product_version_refs of this ProductRest.
        :type: list[ProductVersionRefRest]
        """

        self._product_version_refs = product_version_refs

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
        if not isinstance(other, ProductRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
