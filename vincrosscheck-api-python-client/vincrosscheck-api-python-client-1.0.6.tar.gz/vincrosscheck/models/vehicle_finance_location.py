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


class VehicleFinanceLocation(object):
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
        'branch': 'str',
        'city': 'str',
        'state': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'city': 'city',
        'state': 'state'
    }

    def __init__(self, branch=None, city=None, state=None):  # noqa: E501
        """VehicleFinanceLocation - a model defined in Swagger"""  # noqa: E501

        self._branch = None
        self._city = None
        self._state = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state

    @property
    def branch(self):
        """Gets the branch of this VehicleFinanceLocation.  # noqa: E501

        the ID or name of the branch at which the vehicle is physically located  # noqa: E501

        :return: The branch of this VehicleFinanceLocation.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this VehicleFinanceLocation.

        the ID or name of the branch at which the vehicle is physically located  # noqa: E501

        :param branch: The branch of this VehicleFinanceLocation.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def city(self):
        """Gets the city of this VehicleFinanceLocation.  # noqa: E501

        the city in which the vehicle is physically located  # noqa: E501

        :return: The city of this VehicleFinanceLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this VehicleFinanceLocation.

        the city in which the vehicle is physically located  # noqa: E501

        :param city: The city of this VehicleFinanceLocation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this VehicleFinanceLocation.  # noqa: E501

        the state in which the vehicle is physically located  # noqa: E501

        :return: The state of this VehicleFinanceLocation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VehicleFinanceLocation.

        the state in which the vehicle is physically located  # noqa: E501

        :param state: The state of this VehicleFinanceLocation.  # noqa: E501
        :type: str
        """
        if state is not None and len(state) > 2:
            raise ValueError("Invalid value for `state`, length must be less than or equal to `2`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, VehicleFinanceLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
