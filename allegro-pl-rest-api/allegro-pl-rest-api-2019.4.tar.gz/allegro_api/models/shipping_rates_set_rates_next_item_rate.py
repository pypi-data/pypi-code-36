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


class ShippingRatesSetRatesNextItemRate(object):
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
        'amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, amount=None, currency=None):  # noqa: E501
        """ShippingRatesSetRatesNextItemRate - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._currency = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency

    @property
    def amount(self):
        """Gets the amount of this ShippingRatesSetRatesNextItemRate.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this ShippingRatesSetRatesNextItemRate.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ShippingRatesSetRatesNextItemRate.

        Amount  # noqa: E501

        :param amount: The amount of this ShippingRatesSetRatesNextItemRate.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this ShippingRatesSetRatesNextItemRate.  # noqa: E501

        ISO 4217 currency code  # noqa: E501

        :return: The currency of this ShippingRatesSetRatesNextItemRate.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShippingRatesSetRatesNextItemRate.

        ISO 4217 currency code  # noqa: E501

        :param currency: The currency of this ShippingRatesSetRatesNextItemRate.  # noqa: E501
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, ShippingRatesSetRatesNextItemRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
