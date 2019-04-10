# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BollingerBandsTechnicalValue(object):
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
        'date_time': 'datetime',
        'lower_band': 'float',
        'middle_band': 'float',
        'upper_band': 'float'
    }

    attribute_map = {
        'date_time': 'date_time',
        'lower_band': 'lower_band',
        'middle_band': 'middle_band',
        'upper_band': 'upper_band'
    }

    def __init__(self, date_time=None, lower_band=None, middle_band=None, upper_band=None):  # noqa: E501
        """BollingerBandsTechnicalValue - a model defined in Swagger"""  # noqa: E501

        self._date_time = None
        self._lower_band = None
        self._middle_band = None
        self._upper_band = None
        self.discriminator = None

        if date_time is not None:
            self.date_time = date_time
        if lower_band is not None:
            self.lower_band = lower_band
        if middle_band is not None:
            self.middle_band = middle_band
        if upper_band is not None:
            self.upper_band = upper_band

    @property
    def date_time(self):
        """Gets the date_time of this BollingerBandsTechnicalValue.  # noqa: E501

        The date_time of the observation  # noqa: E501

        :return: The date_time of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time
        
    @property
    def date_time_dict(self):
        """Gets the date_time of this BollingerBandsTechnicalValue.  # noqa: E501

        The date_time of the observation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The date_time of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = getattr(self, date_time)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'date_time': value }

        
        return result
        

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this BollingerBandsTechnicalValue.

        The date_time of the observation  # noqa: E501

        :param date_time: The date_time of this BollingerBandsTechnicalValue.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def lower_band(self):
        """Gets the lower_band of this BollingerBandsTechnicalValue.  # noqa: E501

        The lower band value of the Bollinger Bands technical indicator calculation  # noqa: E501

        :return: The lower_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._lower_band
        
    @property
    def lower_band_dict(self):
        """Gets the lower_band of this BollingerBandsTechnicalValue.  # noqa: E501

        The lower band value of the Bollinger Bands technical indicator calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The lower_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = getattr(self, lower_band)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'lower_band': value }

        
        return result
        

    @lower_band.setter
    def lower_band(self, lower_band):
        """Sets the lower_band of this BollingerBandsTechnicalValue.

        The lower band value of the Bollinger Bands technical indicator calculation  # noqa: E501

        :param lower_band: The lower_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :type: float
        """

        self._lower_band = lower_band

    @property
    def middle_band(self):
        """Gets the middle_band of this BollingerBandsTechnicalValue.  # noqa: E501

        The middle band value of the Bollinger Bands technical indicator calculation  # noqa: E501

        :return: The middle_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._middle_band
        
    @property
    def middle_band_dict(self):
        """Gets the middle_band of this BollingerBandsTechnicalValue.  # noqa: E501

        The middle band value of the Bollinger Bands technical indicator calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The middle_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = getattr(self, middle_band)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'middle_band': value }

        
        return result
        

    @middle_band.setter
    def middle_band(self, middle_band):
        """Sets the middle_band of this BollingerBandsTechnicalValue.

        The middle band value of the Bollinger Bands technical indicator calculation  # noqa: E501

        :param middle_band: The middle_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :type: float
        """

        self._middle_band = middle_band

    @property
    def upper_band(self):
        """Gets the upper_band of this BollingerBandsTechnicalValue.  # noqa: E501

        The upper band value of the Bollinger Bands technical indicator calculation  # noqa: E501

        :return: The upper_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: float
        """
        return self._upper_band
        
    @property
    def upper_band_dict(self):
        """Gets the upper_band of this BollingerBandsTechnicalValue.  # noqa: E501

        The upper band value of the Bollinger Bands technical indicator calculation as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The upper_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :rtype: float
        """

        result = None

        value = getattr(self, upper_band)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'upper_band': value }

        
        return result
        

    @upper_band.setter
    def upper_band(self, upper_band):
        """Sets the upper_band of this BollingerBandsTechnicalValue.

        The upper band value of the Bollinger Bands technical indicator calculation  # noqa: E501

        :param upper_band: The upper_band of this BollingerBandsTechnicalValue.  # noqa: E501
        :type: float
        """

        self._upper_band = upper_band

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
        if not isinstance(other, BollingerBandsTechnicalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
