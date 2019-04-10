# coding: utf-8

"""
    ACI Services API

    API for methods pertaining to all ACI services  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from autocheckinsurance.models.vehicle_history import VehicleHistory  # noqa: F401,E501
from autocheckinsurance.models.vehicle_information import VehicleInformation  # noqa: F401,E501
from autocheckinsurance.models.vehicle_ownership_activity import VehicleOwnershipActivity  # noqa: F401,E501
from autocheckinsurance.models.vehicle_recall import VehicleRecall  # noqa: F401,E501
from autocheckinsurance.models.vehicle_scoring import VehicleScoring  # noqa: F401,E501


class Vehicle(object):
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
        'history': 'VehicleHistory',
        'recalls': 'VehicleRecall',
        'reference_number': 'str',
        'scoring': 'VehicleScoring',
        'vehicle_information': 'VehicleInformation',
        'vehicle_owner_history': 'list[VehicleOwnershipActivity]'
    }

    attribute_map = {
        'history': 'history',
        'recalls': 'recalls',
        'reference_number': 'referenceNumber',
        'scoring': 'scoring',
        'vehicle_information': 'vehicleInformation',
        'vehicle_owner_history': 'vehicleOwnerHistory'
    }

    def __init__(self, history=None, recalls=None, reference_number=None, scoring=None, vehicle_information=None, vehicle_owner_history=None):  # noqa: E501
        """Vehicle - a model defined in Swagger"""  # noqa: E501

        self._history = None
        self._recalls = None
        self._reference_number = None
        self._scoring = None
        self._vehicle_information = None
        self._vehicle_owner_history = None
        self.discriminator = None

        if history is not None:
            self.history = history
        if recalls is not None:
            self.recalls = recalls
        if reference_number is not None:
            self.reference_number = reference_number
        if scoring is not None:
            self.scoring = scoring
        if vehicle_information is not None:
            self.vehicle_information = vehicle_information
        if vehicle_owner_history is not None:
            self.vehicle_owner_history = vehicle_owner_history

    @property
    def history(self):
        """Gets the history of this Vehicle.  # noqa: E501


        :return: The history of this Vehicle.  # noqa: E501
        :rtype: VehicleHistory
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this Vehicle.


        :param history: The history of this Vehicle.  # noqa: E501
        :type: VehicleHistory
        """

        self._history = history

    @property
    def recalls(self):
        """Gets the recalls of this Vehicle.  # noqa: E501

        recall information for the vehicle  # noqa: E501

        :return: The recalls of this Vehicle.  # noqa: E501
        :rtype: VehicleRecall
        """
        return self._recalls

    @recalls.setter
    def recalls(self, recalls):
        """Sets the recalls of this Vehicle.

        recall information for the vehicle  # noqa: E501

        :param recalls: The recalls of this Vehicle.  # noqa: E501
        :type: VehicleRecall
        """

        self._recalls = recalls

    @property
    def reference_number(self):
        """Gets the reference_number of this Vehicle.  # noqa: E501

        the reference number for the caller's tracking purposes  # noqa: E501

        :return: The reference_number of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this Vehicle.

        the reference number for the caller's tracking purposes  # noqa: E501

        :param reference_number: The reference_number of this Vehicle.  # noqa: E501
        :type: str
        """

        self._reference_number = reference_number

    @property
    def scoring(self):
        """Gets the scoring of this Vehicle.  # noqa: E501


        :return: The scoring of this Vehicle.  # noqa: E501
        :rtype: VehicleScoring
        """
        return self._scoring

    @scoring.setter
    def scoring(self, scoring):
        """Sets the scoring of this Vehicle.


        :param scoring: The scoring of this Vehicle.  # noqa: E501
        :type: VehicleScoring
        """

        self._scoring = scoring

    @property
    def vehicle_information(self):
        """Gets the vehicle_information of this Vehicle.  # noqa: E501


        :return: The vehicle_information of this Vehicle.  # noqa: E501
        :rtype: VehicleInformation
        """
        return self._vehicle_information

    @vehicle_information.setter
    def vehicle_information(self, vehicle_information):
        """Sets the vehicle_information of this Vehicle.


        :param vehicle_information: The vehicle_information of this Vehicle.  # noqa: E501
        :type: VehicleInformation
        """

        self._vehicle_information = vehicle_information

    @property
    def vehicle_owner_history(self):
        """Gets the vehicle_owner_history of this Vehicle.  # noqa: E501

        ownership history for the vehicle (Please note that ownership activity is a separately licensed section of the vehicle history responses. Please contact your Red Mountain sales team if you wish to receive ownership activity information)  # noqa: E501

        :return: The vehicle_owner_history of this Vehicle.  # noqa: E501
        :rtype: list[VehicleOwnershipActivity]
        """
        return self._vehicle_owner_history

    @vehicle_owner_history.setter
    def vehicle_owner_history(self, vehicle_owner_history):
        """Sets the vehicle_owner_history of this Vehicle.

        ownership history for the vehicle (Please note that ownership activity is a separately licensed section of the vehicle history responses. Please contact your Red Mountain sales team if you wish to receive ownership activity information)  # noqa: E501

        :param vehicle_owner_history: The vehicle_owner_history of this Vehicle.  # noqa: E501
        :type: list[VehicleOwnershipActivity]
        """

        self._vehicle_owner_history = vehicle_owner_history

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
        if not isinstance(other, Vehicle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
