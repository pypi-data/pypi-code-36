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

from autocheckauctions.models.vehicle_request_attribute import VehicleRequestAttribute  # noqa: F401,E501


class HistoryRequest(object):
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
        'vehicle_request_attributes': 'list[VehicleRequestAttribute]'
    }

    attribute_map = {
        'vehicle_request_attributes': 'vehicleRequestAttributes'
    }

    def __init__(self, vehicle_request_attributes=None):  # noqa: E501
        """HistoryRequest - a model defined in Swagger"""  # noqa: E501

        self._vehicle_request_attributes = None
        self.discriminator = None

        self.vehicle_request_attributes = vehicle_request_attributes

    @property
    def vehicle_request_attributes(self):
        """Gets the vehicle_request_attributes of this HistoryRequest.  # noqa: E501

        the list of vehicle request attributes  # noqa: E501

        :return: The vehicle_request_attributes of this HistoryRequest.  # noqa: E501
        :rtype: list[VehicleRequestAttribute]
        """
        return self._vehicle_request_attributes

    @vehicle_request_attributes.setter
    def vehicle_request_attributes(self, vehicle_request_attributes):
        """Sets the vehicle_request_attributes of this HistoryRequest.

        the list of vehicle request attributes  # noqa: E501

        :param vehicle_request_attributes: The vehicle_request_attributes of this HistoryRequest.  # noqa: E501
        :type: list[VehicleRequestAttribute]
        """
        if vehicle_request_attributes is None:
            raise ValueError("Invalid value for `vehicle_request_attributes`, must not be `None`")  # noqa: E501

        self._vehicle_request_attributes = vehicle_request_attributes

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
        if not isinstance(other, HistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
