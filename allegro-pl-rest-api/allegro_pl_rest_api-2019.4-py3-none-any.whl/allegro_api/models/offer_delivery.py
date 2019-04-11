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


class OfferDelivery(object):
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
        'available_for_free': 'bool',
        'lowest_price': 'OfferLowestPrice'
    }

    attribute_map = {
        'available_for_free': 'availableForFree',
        'lowest_price': 'lowestPrice'
    }

    def __init__(self, available_for_free=None, lowest_price=None):  # noqa: E501
        """OfferDelivery - a model defined in OpenAPI"""  # noqa: E501

        self._available_for_free = None
        self._lowest_price = None
        self.discriminator = None

        if available_for_free is not None:
            self.available_for_free = available_for_free
        if lowest_price is not None:
            self.lowest_price = lowest_price

    @property
    def available_for_free(self):
        """Gets the available_for_free of this OfferDelivery.  # noqa: E501

        Indicates whether the item has free shipping option.  # noqa: E501

        :return: The available_for_free of this OfferDelivery.  # noqa: E501
        :rtype: bool
        """
        return self._available_for_free

    @available_for_free.setter
    def available_for_free(self, available_for_free):
        """Sets the available_for_free of this OfferDelivery.

        Indicates whether the item has free shipping option.  # noqa: E501

        :param available_for_free: The available_for_free of this OfferDelivery.  # noqa: E501
        :type: bool
        """

        self._available_for_free = available_for_free

    @property
    def lowest_price(self):
        """Gets the lowest_price of this OfferDelivery.  # noqa: E501


        :return: The lowest_price of this OfferDelivery.  # noqa: E501
        :rtype: OfferLowestPrice
        """
        return self._lowest_price

    @lowest_price.setter
    def lowest_price(self, lowest_price):
        """Sets the lowest_price of this OfferDelivery.


        :param lowest_price: The lowest_price of this OfferDelivery.  # noqa: E501
        :type: OfferLowestPrice
        """

        self._lowest_price = lowest_price

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
        if not isinstance(other, OfferDelivery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
