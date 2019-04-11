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


class GetSaleProductsResponse(object):
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
        'products': 'list[SaleProductResponseDto]',
        'count': 'float'
    }

    attribute_map = {
        'products': 'products',
        'count': 'count'
    }

    def __init__(self, products=None, count=None):  # noqa: E501
        """GetSaleProductsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._products = None
        self._count = None
        self.discriminator = None

        self.products = products
        if count is not None:
            self.count = count

    @property
    def products(self):
        """Gets the products of this GetSaleProductsResponse.  # noqa: E501


        :return: The products of this GetSaleProductsResponse.  # noqa: E501
        :rtype: list[SaleProductResponseDto]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this GetSaleProductsResponse.


        :param products: The products of this GetSaleProductsResponse.  # noqa: E501
        :type: list[SaleProductResponseDto]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def count(self):
        """Gets the count of this GetSaleProductsResponse.  # noqa: E501

        Total number of products matching query criteria  # noqa: E501

        :return: The count of this GetSaleProductsResponse.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GetSaleProductsResponse.

        Total number of products matching query criteria  # noqa: E501

        :param count: The count of this GetSaleProductsResponse.  # noqa: E501
        :type: float
        """

        self._count = count

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
        if not isinstance(other, GetSaleProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
