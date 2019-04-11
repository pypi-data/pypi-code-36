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


class Location(object):
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
        'city': 'str',
        'country_code': 'str',
        'post_code': 'str',
        'province': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country_code': 'countryCode',
        'post_code': 'postCode',
        'province': 'province'
    }

    def __init__(self, city=None, country_code=None, post_code=None, province=None):  # noqa: E501
        """Location - a model defined in OpenAPI"""  # noqa: E501

        self._city = None
        self._country_code = None
        self._post_code = None
        self._province = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if country_code is not None:
            self.country_code = country_code
        if post_code is not None:
            self.post_code = post_code
        if province is not None:
            self.province = province

    @property
    def city(self):
        """Gets the city of this Location.  # noqa: E501


        :return: The city of this Location.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.


        :param city: The city of this Location.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 50:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `50`")  # noqa: E501

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this Location.  # noqa: E501


        :return: The country_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Location.


        :param country_code: The country_code of this Location.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def post_code(self):
        """Gets the post_code of this Location.  # noqa: E501


        :return: The post_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Location.


        :param post_code: The post_code of this Location.  # noqa: E501
        :type: str
        """

        self._post_code = post_code

    @property
    def province(self):
        """Gets the province of this Location.  # noqa: E501


        :return: The province of this Location.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this Location.


        :param province: The province of this Location.  # noqa: E501
        :type: str
        """
        if province is not None and len(province) > 50:
            raise ValueError("Invalid value for `province`, length must be less than or equal to `50`")  # noqa: E501

        self._province = province

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
