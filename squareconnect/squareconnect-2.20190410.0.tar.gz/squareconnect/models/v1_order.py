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


class V1Order(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, id=None, buyer_email=None, recipient_name=None, recipient_phone_number=None, state=None, shipping_address=None, subtotal_money=None, total_shipping_money=None, total_tax_money=None, total_price_money=None, total_discount_money=None, created_at=None, updated_at=None, expires_at=None, payment_id=None, buyer_note=None, completed_note=None, refunded_note=None, canceled_note=None, tender=None, order_history=None, promo_code=None, btc_receive_address=None, btc_price_satoshi=None):
        """
        V1Order - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[Error]',
            'id': 'str',
            'buyer_email': 'str',
            'recipient_name': 'str',
            'recipient_phone_number': 'str',
            'state': 'str',
            'shipping_address': 'Address',
            'subtotal_money': 'V1Money',
            'total_shipping_money': 'V1Money',
            'total_tax_money': 'V1Money',
            'total_price_money': 'V1Money',
            'total_discount_money': 'V1Money',
            'created_at': 'str',
            'updated_at': 'str',
            'expires_at': 'str',
            'payment_id': 'str',
            'buyer_note': 'str',
            'completed_note': 'str',
            'refunded_note': 'str',
            'canceled_note': 'str',
            'tender': 'V1Tender',
            'order_history': 'list[V1OrderHistoryEntry]',
            'promo_code': 'str',
            'btc_receive_address': 'str',
            'btc_price_satoshi': 'float'
        }

        self.attribute_map = {
            'errors': 'errors',
            'id': 'id',
            'buyer_email': 'buyer_email',
            'recipient_name': 'recipient_name',
            'recipient_phone_number': 'recipient_phone_number',
            'state': 'state',
            'shipping_address': 'shipping_address',
            'subtotal_money': 'subtotal_money',
            'total_shipping_money': 'total_shipping_money',
            'total_tax_money': 'total_tax_money',
            'total_price_money': 'total_price_money',
            'total_discount_money': 'total_discount_money',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'expires_at': 'expires_at',
            'payment_id': 'payment_id',
            'buyer_note': 'buyer_note',
            'completed_note': 'completed_note',
            'refunded_note': 'refunded_note',
            'canceled_note': 'canceled_note',
            'tender': 'tender',
            'order_history': 'order_history',
            'promo_code': 'promo_code',
            'btc_receive_address': 'btc_receive_address',
            'btc_price_satoshi': 'btc_price_satoshi'
        }

        self._errors = errors
        self._id = id
        self._buyer_email = buyer_email
        self._recipient_name = recipient_name
        self._recipient_phone_number = recipient_phone_number
        self._state = state
        self._shipping_address = shipping_address
        self._subtotal_money = subtotal_money
        self._total_shipping_money = total_shipping_money
        self._total_tax_money = total_tax_money
        self._total_price_money = total_price_money
        self._total_discount_money = total_discount_money
        self._created_at = created_at
        self._updated_at = updated_at
        self._expires_at = expires_at
        self._payment_id = payment_id
        self._buyer_note = buyer_note
        self._completed_note = completed_note
        self._refunded_note = refunded_note
        self._canceled_note = canceled_note
        self._tender = tender
        self._order_history = order_history
        self._promo_code = promo_code
        self._btc_receive_address = btc_receive_address
        self._btc_price_satoshi = btc_price_satoshi

    @property
    def errors(self):
        """
        Gets the errors of this V1Order.
        Any errors that occurred during the request.

        :return: The errors of this V1Order.
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this V1Order.
        Any errors that occurred during the request.

        :param errors: The errors of this V1Order.
        :type: list[Error]
        """

        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this V1Order.
        The order's unique identifier.

        :return: The id of this V1Order.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Order.
        The order's unique identifier.

        :param id: The id of this V1Order.
        :type: str
        """

        self._id = id

    @property
    def buyer_email(self):
        """
        Gets the buyer_email of this V1Order.
        The email address of the order's buyer.

        :return: The buyer_email of this V1Order.
        :rtype: str
        """
        return self._buyer_email

    @buyer_email.setter
    def buyer_email(self, buyer_email):
        """
        Sets the buyer_email of this V1Order.
        The email address of the order's buyer.

        :param buyer_email: The buyer_email of this V1Order.
        :type: str
        """

        self._buyer_email = buyer_email

    @property
    def recipient_name(self):
        """
        Gets the recipient_name of this V1Order.
        The name of the order's buyer.

        :return: The recipient_name of this V1Order.
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """
        Sets the recipient_name of this V1Order.
        The name of the order's buyer.

        :param recipient_name: The recipient_name of this V1Order.
        :type: str
        """

        self._recipient_name = recipient_name

    @property
    def recipient_phone_number(self):
        """
        Gets the recipient_phone_number of this V1Order.
        The phone number to use for the order's delivery.

        :return: The recipient_phone_number of this V1Order.
        :rtype: str
        """
        return self._recipient_phone_number

    @recipient_phone_number.setter
    def recipient_phone_number(self, recipient_phone_number):
        """
        Sets the recipient_phone_number of this V1Order.
        The phone number to use for the order's delivery.

        :param recipient_phone_number: The recipient_phone_number of this V1Order.
        :type: str
        """

        self._recipient_phone_number = recipient_phone_number

    @property
    def state(self):
        """
        Gets the state of this V1Order.
        Whether the tax is an ADDITIVE tax or an INCLUSIVE tax. See [V1OrderState](#type-v1orderstate) for possible values

        :return: The state of this V1Order.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this V1Order.
        Whether the tax is an ADDITIVE tax or an INCLUSIVE tax. See [V1OrderState](#type-v1orderstate) for possible values

        :param state: The state of this V1Order.
        :type: str
        """

        self._state = state

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this V1Order.
        The address to ship the order to.

        :return: The shipping_address of this V1Order.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this V1Order.
        The address to ship the order to.

        :param shipping_address: The shipping_address of this V1Order.
        :type: Address
        """

        self._shipping_address = shipping_address

    @property
    def subtotal_money(self):
        """
        Gets the subtotal_money of this V1Order.
        The amount of all items purchased in the order, before taxes and shipping.

        :return: The subtotal_money of this V1Order.
        :rtype: V1Money
        """
        return self._subtotal_money

    @subtotal_money.setter
    def subtotal_money(self, subtotal_money):
        """
        Sets the subtotal_money of this V1Order.
        The amount of all items purchased in the order, before taxes and shipping.

        :param subtotal_money: The subtotal_money of this V1Order.
        :type: V1Money
        """

        self._subtotal_money = subtotal_money

    @property
    def total_shipping_money(self):
        """
        Gets the total_shipping_money of this V1Order.
        The shipping cost for the order.

        :return: The total_shipping_money of this V1Order.
        :rtype: V1Money
        """
        return self._total_shipping_money

    @total_shipping_money.setter
    def total_shipping_money(self, total_shipping_money):
        """
        Sets the total_shipping_money of this V1Order.
        The shipping cost for the order.

        :param total_shipping_money: The total_shipping_money of this V1Order.
        :type: V1Money
        """

        self._total_shipping_money = total_shipping_money

    @property
    def total_tax_money(self):
        """
        Gets the total_tax_money of this V1Order.
        The total of all taxes applied to the order.

        :return: The total_tax_money of this V1Order.
        :rtype: V1Money
        """
        return self._total_tax_money

    @total_tax_money.setter
    def total_tax_money(self, total_tax_money):
        """
        Sets the total_tax_money of this V1Order.
        The total of all taxes applied to the order.

        :param total_tax_money: The total_tax_money of this V1Order.
        :type: V1Money
        """

        self._total_tax_money = total_tax_money

    @property
    def total_price_money(self):
        """
        Gets the total_price_money of this V1Order.
        The total cost of the order.

        :return: The total_price_money of this V1Order.
        :rtype: V1Money
        """
        return self._total_price_money

    @total_price_money.setter
    def total_price_money(self, total_price_money):
        """
        Sets the total_price_money of this V1Order.
        The total cost of the order.

        :param total_price_money: The total_price_money of this V1Order.
        :type: V1Money
        """

        self._total_price_money = total_price_money

    @property
    def total_discount_money(self):
        """
        Gets the total_discount_money of this V1Order.
        The total of all discounts applied to the order.

        :return: The total_discount_money of this V1Order.
        :rtype: V1Money
        """
        return self._total_discount_money

    @total_discount_money.setter
    def total_discount_money(self, total_discount_money):
        """
        Sets the total_discount_money of this V1Order.
        The total of all discounts applied to the order.

        :param total_discount_money: The total_discount_money of this V1Order.
        :type: V1Money
        """

        self._total_discount_money = total_discount_money

    @property
    def created_at(self):
        """
        Gets the created_at of this V1Order.
        The time when the order was created, in ISO 8601 format.

        :return: The created_at of this V1Order.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this V1Order.
        The time when the order was created, in ISO 8601 format.

        :param created_at: The created_at of this V1Order.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this V1Order.
        The time when the order was last modified, in ISO 8601 format.

        :return: The updated_at of this V1Order.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this V1Order.
        The time when the order was last modified, in ISO 8601 format.

        :param updated_at: The updated_at of this V1Order.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def expires_at(self):
        """
        Gets the expires_at of this V1Order.
        The time when the order expires if no action is taken, in ISO 8601 format.

        :return: The expires_at of this V1Order.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """
        Sets the expires_at of this V1Order.
        The time when the order expires if no action is taken, in ISO 8601 format.

        :param expires_at: The expires_at of this V1Order.
        :type: str
        """

        self._expires_at = expires_at

    @property
    def payment_id(self):
        """
        Gets the payment_id of this V1Order.
        The unique identifier of the payment associated with the order.

        :return: The payment_id of this V1Order.
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """
        Sets the payment_id of this V1Order.
        The unique identifier of the payment associated with the order.

        :param payment_id: The payment_id of this V1Order.
        :type: str
        """

        self._payment_id = payment_id

    @property
    def buyer_note(self):
        """
        Gets the buyer_note of this V1Order.
        A note provided by the buyer when the order was created, if any.

        :return: The buyer_note of this V1Order.
        :rtype: str
        """
        return self._buyer_note

    @buyer_note.setter
    def buyer_note(self, buyer_note):
        """
        Sets the buyer_note of this V1Order.
        A note provided by the buyer when the order was created, if any.

        :param buyer_note: The buyer_note of this V1Order.
        :type: str
        """

        self._buyer_note = buyer_note

    @property
    def completed_note(self):
        """
        Gets the completed_note of this V1Order.
        A note provided by the merchant when the order's state was set to COMPLETED, if any

        :return: The completed_note of this V1Order.
        :rtype: str
        """
        return self._completed_note

    @completed_note.setter
    def completed_note(self, completed_note):
        """
        Sets the completed_note of this V1Order.
        A note provided by the merchant when the order's state was set to COMPLETED, if any

        :param completed_note: The completed_note of this V1Order.
        :type: str
        """

        self._completed_note = completed_note

    @property
    def refunded_note(self):
        """
        Gets the refunded_note of this V1Order.
        A note provided by the merchant when the order's state was set to REFUNDED, if any.

        :return: The refunded_note of this V1Order.
        :rtype: str
        """
        return self._refunded_note

    @refunded_note.setter
    def refunded_note(self, refunded_note):
        """
        Sets the refunded_note of this V1Order.
        A note provided by the merchant when the order's state was set to REFUNDED, if any.

        :param refunded_note: The refunded_note of this V1Order.
        :type: str
        """

        self._refunded_note = refunded_note

    @property
    def canceled_note(self):
        """
        Gets the canceled_note of this V1Order.
        A note provided by the merchant when the order's state was set to CANCELED, if any.

        :return: The canceled_note of this V1Order.
        :rtype: str
        """
        return self._canceled_note

    @canceled_note.setter
    def canceled_note(self, canceled_note):
        """
        Sets the canceled_note of this V1Order.
        A note provided by the merchant when the order's state was set to CANCELED, if any.

        :param canceled_note: The canceled_note of this V1Order.
        :type: str
        """

        self._canceled_note = canceled_note

    @property
    def tender(self):
        """
        Gets the tender of this V1Order.
        The tender used to pay for the order.

        :return: The tender of this V1Order.
        :rtype: V1Tender
        """
        return self._tender

    @tender.setter
    def tender(self, tender):
        """
        Sets the tender of this V1Order.
        The tender used to pay for the order.

        :param tender: The tender of this V1Order.
        :type: V1Tender
        """

        self._tender = tender

    @property
    def order_history(self):
        """
        Gets the order_history of this V1Order.
        The history of actions associated with the order.

        :return: The order_history of this V1Order.
        :rtype: list[V1OrderHistoryEntry]
        """
        return self._order_history

    @order_history.setter
    def order_history(self, order_history):
        """
        Sets the order_history of this V1Order.
        The history of actions associated with the order.

        :param order_history: The order_history of this V1Order.
        :type: list[V1OrderHistoryEntry]
        """

        self._order_history = order_history

    @property
    def promo_code(self):
        """
        Gets the promo_code of this V1Order.
        The promo code provided by the buyer, if any.

        :return: The promo_code of this V1Order.
        :rtype: str
        """
        return self._promo_code

    @promo_code.setter
    def promo_code(self, promo_code):
        """
        Sets the promo_code of this V1Order.
        The promo code provided by the buyer, if any.

        :param promo_code: The promo_code of this V1Order.
        :type: str
        """

        self._promo_code = promo_code

    @property
    def btc_receive_address(self):
        """
        Gets the btc_receive_address of this V1Order.
        For Bitcoin transactions, the address that the buyer sent Bitcoin to.

        :return: The btc_receive_address of this V1Order.
        :rtype: str
        """
        return self._btc_receive_address

    @btc_receive_address.setter
    def btc_receive_address(self, btc_receive_address):
        """
        Sets the btc_receive_address of this V1Order.
        For Bitcoin transactions, the address that the buyer sent Bitcoin to.

        :param btc_receive_address: The btc_receive_address of this V1Order.
        :type: str
        """

        self._btc_receive_address = btc_receive_address

    @property
    def btc_price_satoshi(self):
        """
        Gets the btc_price_satoshi of this V1Order.
        For Bitcoin transactions, the price of the buyer's order in satoshi (100 million satoshi equals 1 BTC).

        :return: The btc_price_satoshi of this V1Order.
        :rtype: float
        """
        return self._btc_price_satoshi

    @btc_price_satoshi.setter
    def btc_price_satoshi(self, btc_price_satoshi):
        """
        Sets the btc_price_satoshi of this V1Order.
        For Bitcoin transactions, the price of the buyer's order in satoshi (100 million satoshi equals 1 BTC).

        :param btc_price_satoshi: The btc_price_satoshi of this V1Order.
        :type: float
        """

        self._btc_price_satoshi = btc_price_satoshi

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
