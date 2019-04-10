# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class Card(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, card_brand=None, last_4=None, exp_month=None, exp_year=None, cardholder_name=None, billing_address=None, fingerprint=None):
        """
        Card - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'card_brand': 'str',
            'last_4': 'str',
            'exp_month': 'int',
            'exp_year': 'int',
            'cardholder_name': 'str',
            'billing_address': 'Address',
            'fingerprint': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'card_brand': 'card_brand',
            'last_4': 'last_4',
            'exp_month': 'exp_month',
            'exp_year': 'exp_year',
            'cardholder_name': 'cardholder_name',
            'billing_address': 'billing_address',
            'fingerprint': 'fingerprint'
        }

        self._id = id
        self._card_brand = card_brand
        self._last_4 = last_4
        self._exp_month = exp_month
        self._exp_year = exp_year
        self._cardholder_name = cardholder_name
        self._billing_address = billing_address
        self._fingerprint = fingerprint

    @property
    def id(self):
        """
        Gets the id of this Card.
        Unique ID for this card. Generated by Square.

        :return: The id of this Card.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Card.
        Unique ID for this card. Generated by Square.

        :param id: The id of this Card.
        :type: str
        """

        self._id = id

    @property
    def card_brand(self):
        """
        Gets the card_brand of this Card.
        The card's brand (such as `VISA`). See [CardBrand](#type-cardbrand) for possible values

        :return: The card_brand of this Card.
        :rtype: str
        """
        return self._card_brand

    @card_brand.setter
    def card_brand(self, card_brand):
        """
        Sets the card_brand of this Card.
        The card's brand (such as `VISA`). See [CardBrand](#type-cardbrand) for possible values

        :param card_brand: The card_brand of this Card.
        :type: str
        """

        self._card_brand = card_brand

    @property
    def last_4(self):
        """
        Gets the last_4 of this Card.
        The last 4 digits of the card number.

        :return: The last_4 of this Card.
        :rtype: str
        """
        return self._last_4

    @last_4.setter
    def last_4(self, last_4):
        """
        Sets the last_4 of this Card.
        The last 4 digits of the card number.

        :param last_4: The last_4 of this Card.
        :type: str
        """

        self._last_4 = last_4

    @property
    def exp_month(self):
        """
        Gets the exp_month of this Card.
        The expiration month of the associated card as an integer between 1 and 12.

        :return: The exp_month of this Card.
        :rtype: int
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """
        Sets the exp_month of this Card.
        The expiration month of the associated card as an integer between 1 and 12.

        :param exp_month: The exp_month of this Card.
        :type: int
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """
        Gets the exp_year of this Card.
        The four-digit year of the card's expiration date.

        :return: The exp_year of this Card.
        :rtype: int
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """
        Sets the exp_year of this Card.
        The four-digit year of the card's expiration date.

        :param exp_year: The exp_year of this Card.
        :type: int
        """

        self._exp_year = exp_year

    @property
    def cardholder_name(self):
        """
        Gets the cardholder_name of this Card.
        The name of the cardholder.

        :return: The cardholder_name of this Card.
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """
        Sets the cardholder_name of this Card.
        The name of the cardholder.

        :param cardholder_name: The cardholder_name of this Card.
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def billing_address(self):
        """
        Gets the billing_address of this Card.
        The billing address for this card.

        :return: The billing_address of this Card.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this Card.
        The billing address for this card.

        :param billing_address: The billing_address of this Card.
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this Card.
        __Not currently set.__ Intended as a Square-assigned identifier, based on the card number, to identify the card across multiple locations within a single application.

        :return: The fingerprint of this Card.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this Card.
        __Not currently set.__ Intended as a Square-assigned identifier, based on the card number, to identify the card across multiple locations within a single application.

        :param fingerprint: The fingerprint of this Card.
        :type: str
        """

        self._fingerprint = fingerprint

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
