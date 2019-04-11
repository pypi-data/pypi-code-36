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


class OrderEventData(object):
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
        'seller': 'SellerReference',
        'buyer': 'BuyerReference',
        'line_items': 'list[OrderLineItem]',
        'checkout_form': 'CheckoutFormReference'
    }

    attribute_map = {
        'seller': 'seller',
        'buyer': 'buyer',
        'line_items': 'lineItems',
        'checkout_form': 'checkoutForm'
    }

    def __init__(self, seller=None, buyer=None, line_items=None, checkout_form=None):  # noqa: E501
        """OrderEventData - a model defined in OpenAPI"""  # noqa: E501

        self._seller = None
        self._buyer = None
        self._line_items = None
        self._checkout_form = None
        self.discriminator = None

        self.seller = seller
        self.buyer = buyer
        self.line_items = line_items
        if checkout_form is not None:
            self.checkout_form = checkout_form

    @property
    def seller(self):
        """Gets the seller of this OrderEventData.  # noqa: E501


        :return: The seller of this OrderEventData.  # noqa: E501
        :rtype: SellerReference
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this OrderEventData.


        :param seller: The seller of this OrderEventData.  # noqa: E501
        :type: SellerReference
        """
        if seller is None:
            raise ValueError("Invalid value for `seller`, must not be `None`")  # noqa: E501

        self._seller = seller

    @property
    def buyer(self):
        """Gets the buyer of this OrderEventData.  # noqa: E501


        :return: The buyer of this OrderEventData.  # noqa: E501
        :rtype: BuyerReference
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this OrderEventData.


        :param buyer: The buyer of this OrderEventData.  # noqa: E501
        :type: BuyerReference
        """
        if buyer is None:
            raise ValueError("Invalid value for `buyer`, must not be `None`")  # noqa: E501

        self._buyer = buyer

    @property
    def line_items(self):
        """Gets the line_items of this OrderEventData.  # noqa: E501


        :return: The line_items of this OrderEventData.  # noqa: E501
        :rtype: list[OrderLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this OrderEventData.


        :param line_items: The line_items of this OrderEventData.  # noqa: E501
        :type: list[OrderLineItem]
        """
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")  # noqa: E501

        self._line_items = line_items

    @property
    def checkout_form(self):
        """Gets the checkout_form of this OrderEventData.  # noqa: E501


        :return: The checkout_form of this OrderEventData.  # noqa: E501
        :rtype: CheckoutFormReference
        """
        return self._checkout_form

    @checkout_form.setter
    def checkout_form(self, checkout_form):
        """Sets the checkout_form of this OrderEventData.


        :param checkout_form: The checkout_form of this OrderEventData.  # noqa: E501
        :type: CheckoutFormReference
        """

        self._checkout_form = checkout_form

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
        if not isinstance(other, OrderEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
