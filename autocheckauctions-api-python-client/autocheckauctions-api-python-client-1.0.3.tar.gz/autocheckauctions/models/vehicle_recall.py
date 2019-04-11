# coding: utf-8

"""
    ACA Services API

    API for methods pertaining to all ACA services  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from autocheckauctions.models.recall_record import RecallRecord  # noqa: F401,E501


class VehicleRecall(object):
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
        'count': 'int',
        'manufacturer_url': 'str',
        'recall_records': 'list[RecallRecord]'
    }

    attribute_map = {
        'count': 'count',
        'manufacturer_url': 'manufacturerURL',
        'recall_records': 'recallRecords'
    }

    def __init__(self, count=None, manufacturer_url=None, recall_records=None):  # noqa: E501
        """VehicleRecall - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._manufacturer_url = None
        self._recall_records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if manufacturer_url is not None:
            self.manufacturer_url = manufacturer_url
        if recall_records is not None:
            self.recall_records = recall_records

    @property
    def count(self):
        """Gets the count of this VehicleRecall.  # noqa: E501

        the number of recall records  # noqa: E501

        :return: The count of this VehicleRecall.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VehicleRecall.

        the number of recall records  # noqa: E501

        :param count: The count of this VehicleRecall.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def manufacturer_url(self):
        """Gets the manufacturer_url of this VehicleRecall.  # noqa: E501

        the manufacturer's URL  # noqa: E501

        :return: The manufacturer_url of this VehicleRecall.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_url

    @manufacturer_url.setter
    def manufacturer_url(self, manufacturer_url):
        """Sets the manufacturer_url of this VehicleRecall.

        the manufacturer's URL  # noqa: E501

        :param manufacturer_url: The manufacturer_url of this VehicleRecall.  # noqa: E501
        :type: str
        """

        self._manufacturer_url = manufacturer_url

    @property
    def recall_records(self):
        """Gets the recall_records of this VehicleRecall.  # noqa: E501

        the list of recalls for the vehicle  # noqa: E501

        :return: The recall_records of this VehicleRecall.  # noqa: E501
        :rtype: list[RecallRecord]
        """
        return self._recall_records

    @recall_records.setter
    def recall_records(self, recall_records):
        """Sets the recall_records of this VehicleRecall.

        the list of recalls for the vehicle  # noqa: E501

        :param recall_records: The recall_records of this VehicleRecall.  # noqa: E501
        :type: list[RecallRecord]
        """

        self._recall_records = recall_records

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
        if not isinstance(other, VehicleRecall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
