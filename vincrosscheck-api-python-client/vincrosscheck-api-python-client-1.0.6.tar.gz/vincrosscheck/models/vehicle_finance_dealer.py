# coding: utf-8

"""
    VXC Services API

    API for methods pertaining to all VXC services  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VehicleFinanceDealer(object):
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
        'auction_access_id': 'int',
        'name': 'str',
        'number': 'str'
    }

    attribute_map = {
        'auction_access_id': 'auctionAccessId',
        'name': 'name',
        'number': 'number'
    }

    def __init__(self, auction_access_id=None, name=None, number=None):  # noqa: E501
        """VehicleFinanceDealer - a model defined in Swagger"""  # noqa: E501

        self._auction_access_id = None
        self._name = None
        self._number = None
        self.discriminator = None

        if auction_access_id is not None:
            self.auction_access_id = auction_access_id
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number

    @property
    def auction_access_id(self):
        """Gets the auction_access_id of this VehicleFinanceDealer.  # noqa: E501

        the AuctionACCESS ID of the company – for customers licensed with AuctionACCESS  # noqa: E501

        :return: The auction_access_id of this VehicleFinanceDealer.  # noqa: E501
        :rtype: int
        """
        return self._auction_access_id

    @auction_access_id.setter
    def auction_access_id(self, auction_access_id):
        """Sets the auction_access_id of this VehicleFinanceDealer.

        the AuctionACCESS ID of the company – for customers licensed with AuctionACCESS  # noqa: E501

        :param auction_access_id: The auction_access_id of this VehicleFinanceDealer.  # noqa: E501
        :type: int
        """

        self._auction_access_id = auction_access_id

    @property
    def name(self):
        """Gets the name of this VehicleFinanceDealer.  # noqa: E501

        the name of the company  # noqa: E501

        :return: The name of this VehicleFinanceDealer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleFinanceDealer.

        the name of the company  # noqa: E501

        :param name: The name of this VehicleFinanceDealer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this VehicleFinanceDealer.  # noqa: E501

        the ID by which your company recognizes the company  # noqa: E501

        :return: The number of this VehicleFinanceDealer.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this VehicleFinanceDealer.

        the ID by which your company recognizes the company  # noqa: E501

        :param number: The number of this VehicleFinanceDealer.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if not isinstance(other, VehicleFinanceDealer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
