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


class CheckoutFormDeliveryPickupPointAddress(object):
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
        'street': 'str',
        'zip_code': 'str',
        'city': 'str'
    }

    attribute_map = {
        'street': 'street',
        'zip_code': 'zipCode',
        'city': 'city'
    }

    def __init__(self, street=None, zip_code=None, city=None):  # noqa: E501
        """CheckoutFormDeliveryPickupPointAddress - a model defined in OpenAPI"""  # noqa: E501

        self._street = None
        self._zip_code = None
        self._city = None
        self.discriminator = None

        if street is not None:
            self.street = street
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city

    @property
    def street(self):
        """Gets the street of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501

        Delivery point street name  # noqa: E501

        :return: The street of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this CheckoutFormDeliveryPickupPointAddress.

        Delivery point street name  # noqa: E501

        :param street: The street of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def zip_code(self):
        """Gets the zip_code of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501

        Delivery point postal code  # noqa: E501

        :return: The zip_code of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this CheckoutFormDeliveryPickupPointAddress.

        Delivery point postal code  # noqa: E501

        :param zip_code: The zip_code of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501

        City name  # noqa: E501

        :return: The city of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CheckoutFormDeliveryPickupPointAddress.

        City name  # noqa: E501

        :param city: The city of this CheckoutFormDeliveryPickupPointAddress.  # noqa: E501
        :type: str
        """

        self._city = city

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
        if not isinstance(other, CheckoutFormDeliveryPickupPointAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
