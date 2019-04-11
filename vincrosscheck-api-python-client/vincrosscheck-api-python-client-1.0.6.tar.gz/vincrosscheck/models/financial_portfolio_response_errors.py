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

from vincrosscheck.models.vehicle_finance_record import VehicleFinanceRecord  # noqa: F401,E501


class FinancialPortfolioResponseErrors(object):
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
        'message': 'str',
        'record': 'VehicleFinanceRecord'
    }

    attribute_map = {
        'message': 'message',
        'record': 'record'
    }

    def __init__(self, message=None, record=None):  # noqa: E501
        """FinancialPortfolioResponseErrors - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._record = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if record is not None:
            self.record = record

    @property
    def message(self):
        """Gets the message of this FinancialPortfolioResponseErrors.  # noqa: E501

        the cause of the error  # noqa: E501

        :return: The message of this FinancialPortfolioResponseErrors.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FinancialPortfolioResponseErrors.

        the cause of the error  # noqa: E501

        :param message: The message of this FinancialPortfolioResponseErrors.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def record(self):
        """Gets the record of this FinancialPortfolioResponseErrors.  # noqa: E501


        :return: The record of this FinancialPortfolioResponseErrors.  # noqa: E501
        :rtype: VehicleFinanceRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this FinancialPortfolioResponseErrors.


        :param record: The record of this FinancialPortfolioResponseErrors.  # noqa: E501
        :type: VehicleFinanceRecord
        """

        self._record = record

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
        if not isinstance(other, FinancialPortfolioResponseErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
