# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.5
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyObjectsResponse(object):
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
        'pagination_info': 'PaginationInfo',
        'items': 'list[PolicyObjects]'
    }

    attribute_map = {
        'pagination_info': 'pagination_info',
        'items': 'items'
    }

    def __init__(self, pagination_info=None, items=None):
        """
        PolicyObjectsResponse - a model defined in Swagger
        """

        self._pagination_info = None
        self._items = None

        if pagination_info is not None:
          self.pagination_info = pagination_info
        if items is not None:
          self.items = items

    @property
    def pagination_info(self):
        """
        Gets the pagination_info of this PolicyObjectsResponse.
        pagination information, only available in GET requests

        :return: The pagination_info of this PolicyObjectsResponse.
        :rtype: PaginationInfo
        """
        return self._pagination_info

    @pagination_info.setter
    def pagination_info(self, pagination_info):
        """
        Sets the pagination_info of this PolicyObjectsResponse.
        pagination information, only available in GET requests

        :param pagination_info: The pagination_info of this PolicyObjectsResponse.
        :type: PaginationInfo
        """

        self._pagination_info = pagination_info

    @property
    def items(self):
        """
        Gets the items of this PolicyObjectsResponse.
        a list of policies attached to file systems

        :return: The items of this PolicyObjectsResponse.
        :rtype: list[PolicyObjects]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PolicyObjectsResponse.
        a list of policies attached to file systems

        :param items: The items of this PolicyObjectsResponse.
        :type: list[PolicyObjects]
        """

        self._items = items

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
        if not isinstance(other, PolicyObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
