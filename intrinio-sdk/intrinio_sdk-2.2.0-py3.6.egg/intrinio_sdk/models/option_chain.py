# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.option import Option  # noqa: F401,E501
from intrinio_sdk.models.option_price import OptionPrice  # noqa: F401,E501


class OptionChain(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'option': 'Option',
        'price': 'OptionPrice'
    }

    attribute_map = {
        'option': 'option',
        'price': 'price'
    }

    def __init__(self, option=None, price=None):  # noqa: E501
        """OptionChain - a model defined in Swagger"""  # noqa: E501

        self._option = None
        self._price = None
        self.discriminator = None

        if option is not None:
            self.option = option
        if price is not None:
            self.price = price

    @property
    def option(self):
        """Gets the option of this OptionChain.  # noqa: E501


        :return: The option of this OptionChain.  # noqa: E501
        :rtype: Option
        """
        return self._option
        
    @property
    def option_dict(self):
        """Gets the option of this OptionChain.  # noqa: E501


        :return: The option of this OptionChain.  # noqa: E501
        :rtype: Option
        """

        result = None

        value = self.option
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'option': value }

        
        return result
        

    @option.setter
    def option(self, option):
        """Sets the option of this OptionChain.


        :param option: The option of this OptionChain.  # noqa: E501
        :type: Option
        """

        self._option = option

    @property
    def price(self):
        """Gets the price of this OptionChain.  # noqa: E501


        :return: The price of this OptionChain.  # noqa: E501
        :rtype: OptionPrice
        """
        return self._price
        
    @property
    def price_dict(self):
        """Gets the price of this OptionChain.  # noqa: E501


        :return: The price of this OptionChain.  # noqa: E501
        :rtype: OptionPrice
        """

        result = None

        value = self.price
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'price': value }

        
        return result
        

    @price.setter
    def price(self, price):
        """Sets the price of this OptionChain.


        :param price: The price of this OptionChain.  # noqa: E501
        :type: OptionPrice
        """

        self._price = price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, OptionChain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
