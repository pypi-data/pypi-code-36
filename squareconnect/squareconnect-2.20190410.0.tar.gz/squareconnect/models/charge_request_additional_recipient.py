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


class ChargeRequestAdditionalRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location_id=None, description=None, amount_money=None):
        """
        ChargeRequestAdditionalRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'location_id': 'str',
            'description': 'str',
            'amount_money': 'Money'
        }

        self.attribute_map = {
            'location_id': 'location_id',
            'description': 'description',
            'amount_money': 'amount_money'
        }

        self._location_id = location_id
        self._description = description
        self._amount_money = amount_money

    @property
    def location_id(self):
        """
        Gets the location_id of this ChargeRequestAdditionalRecipient.
        The location ID for a recipient (other than the merchant) receiving a portion of the tender.

        :return: The location_id of this ChargeRequestAdditionalRecipient.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this ChargeRequestAdditionalRecipient.
        The location ID for a recipient (other than the merchant) receiving a portion of the tender.

        :param location_id: The location_id of this ChargeRequestAdditionalRecipient.
        :type: str
        """

        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")
        if len(location_id) > 50:
            raise ValueError("Invalid value for `location_id`, length must be less than `50`")
        if len(location_id) < 1:
            raise ValueError("Invalid value for `location_id`, length must be greater than or equal to `1`")

        self._location_id = location_id

    @property
    def description(self):
        """
        Gets the description of this ChargeRequestAdditionalRecipient.
        The description of the additional recipient.

        :return: The description of this ChargeRequestAdditionalRecipient.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ChargeRequestAdditionalRecipient.
        The description of the additional recipient.

        :param description: The description of this ChargeRequestAdditionalRecipient.
        :type: str
        """

        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")
        if len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than `100`")
        if len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")

        self._description = description

    @property
    def amount_money(self):
        """
        Gets the amount_money of this ChargeRequestAdditionalRecipient.
        The amount of money distributed to the recipient.

        :return: The amount_money of this ChargeRequestAdditionalRecipient.
        :rtype: Money
        """
        return self._amount_money

    @amount_money.setter
    def amount_money(self, amount_money):
        """
        Sets the amount_money of this ChargeRequestAdditionalRecipient.
        The amount of money distributed to the recipient.

        :param amount_money: The amount_money of this ChargeRequestAdditionalRecipient.
        :type: Money
        """

        self._amount_money = amount_money

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
