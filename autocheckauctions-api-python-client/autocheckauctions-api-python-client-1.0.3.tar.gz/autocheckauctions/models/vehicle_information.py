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


class VehicleInformation(object):
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
        'body': 'str',
        'country': 'str',
        'engine': 'str',
        'manufacturer': 'str',
        'manufacturer_code': 'str',
        'model': 'str',
        'result_code': 'int',
        'result_message': 'str',
        'series_code': 'str',
        'vehicle_class': 'str',
        'vin': 'str',
        'year': 'str'
    }

    attribute_map = {
        'body': 'body',
        'country': 'country',
        'engine': 'engine',
        'manufacturer': 'manufacturer',
        'manufacturer_code': 'manufacturerCode',
        'model': 'model',
        'result_code': 'resultCode',
        'result_message': 'resultMessage',
        'series_code': 'seriesCode',
        'vehicle_class': 'vehicleClass',
        'vin': 'vin',
        'year': 'year'
    }

    def __init__(self, body=None, country=None, engine=None, manufacturer=None, manufacturer_code=None, model=None, result_code=None, result_message=None, series_code=None, vehicle_class=None, vin=None, year=None):  # noqa: E501
        """VehicleInformation - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._country = None
        self._engine = None
        self._manufacturer = None
        self._manufacturer_code = None
        self._model = None
        self._result_code = None
        self._result_message = None
        self._series_code = None
        self._vehicle_class = None
        self._vin = None
        self._year = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if country is not None:
            self.country = country
        if engine is not None:
            self.engine = engine
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_code is not None:
            self.manufacturer_code = manufacturer_code
        if model is not None:
            self.model = model
        if result_code is not None:
            self.result_code = result_code
        if result_message is not None:
            self.result_message = result_message
        if series_code is not None:
            self.series_code = series_code
        if vehicle_class is not None:
            self.vehicle_class = vehicle_class
        if vin is not None:
            self.vin = vin
        if year is not None:
            self.year = year

    @property
    def body(self):
        """Gets the body of this VehicleInformation.  # noqa: E501

        the body type  # noqa: E501

        :return: The body of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this VehicleInformation.

        the body type  # noqa: E501

        :param body: The body of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def country(self):
        """Gets the country of this VehicleInformation.  # noqa: E501

        the country of origin  # noqa: E501

        :return: The country of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this VehicleInformation.

        the country of origin  # noqa: E501

        :param country: The country of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def engine(self):
        """Gets the engine of this VehicleInformation.  # noqa: E501

        the engine type/size  # noqa: E501

        :return: The engine of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this VehicleInformation.

        the engine type/size  # noqa: E501

        :param engine: The engine of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._engine = engine

    @property
    def manufacturer(self):
        """Gets the manufacturer of this VehicleInformation.  # noqa: E501

        the vehicle manufacturer  # noqa: E501

        :return: The manufacturer of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this VehicleInformation.

        the vehicle manufacturer  # noqa: E501

        :param manufacturer: The manufacturer of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_code(self):
        """Gets the manufacturer_code of this VehicleInformation.  # noqa: E501

        the vehicle manufacturer code  # noqa: E501

        :return: The manufacturer_code of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_code

    @manufacturer_code.setter
    def manufacturer_code(self, manufacturer_code):
        """Sets the manufacturer_code of this VehicleInformation.

        the vehicle manufacturer code  # noqa: E501

        :param manufacturer_code: The manufacturer_code of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._manufacturer_code = manufacturer_code

    @property
    def model(self):
        """Gets the model of this VehicleInformation.  # noqa: E501

        the vehicle model  # noqa: E501

        :return: The model of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this VehicleInformation.

        the vehicle model  # noqa: E501

        :param model: The model of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def result_code(self):
        """Gets the result_code of this VehicleInformation.  # noqa: E501

        the result code (0 = no errors)  # noqa: E501

        :return: The result_code of this VehicleInformation.  # noqa: E501
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this VehicleInformation.

        the result code (0 = no errors)  # noqa: E501

        :param result_code: The result_code of this VehicleInformation.  # noqa: E501
        :type: int
        """

        self._result_code = result_code

    @property
    def result_message(self):
        """Gets the result_message of this VehicleInformation.  # noqa: E501

        the result message. Possible values include:  'No error.', 'Invalid check-digit: The VIN contains an invalid year for the make and model.', 'Invalid check-digit:', 'Warning the VIN pattern is unknown. * Invalid check-digit: The VIN is greater than 17 characters in length.', 'Invalid check-digit: The VIN is less than 17 characters in length.'  # noqa: E501

        :return: The result_message of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._result_message

    @result_message.setter
    def result_message(self, result_message):
        """Sets the result_message of this VehicleInformation.

        the result message. Possible values include:  'No error.', 'Invalid check-digit: The VIN contains an invalid year for the make and model.', 'Invalid check-digit:', 'Warning the VIN pattern is unknown. * Invalid check-digit: The VIN is greater than 17 characters in length.', 'Invalid check-digit: The VIN is less than 17 characters in length.'  # noqa: E501

        :param result_message: The result_message of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._result_message = result_message

    @property
    def series_code(self):
        """Gets the series_code of this VehicleInformation.  # noqa: E501

        the series code  # noqa: E501

        :return: The series_code of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._series_code

    @series_code.setter
    def series_code(self, series_code):
        """Sets the series_code of this VehicleInformation.

        the series code  # noqa: E501

        :param series_code: The series_code of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._series_code = series_code

    @property
    def vehicle_class(self):
        """Gets the vehicle_class of this VehicleInformation.  # noqa: E501

        the vehicle class  # noqa: E501

        :return: The vehicle_class of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_class

    @vehicle_class.setter
    def vehicle_class(self, vehicle_class):
        """Sets the vehicle_class of this VehicleInformation.

        the vehicle class  # noqa: E501

        :param vehicle_class: The vehicle_class of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._vehicle_class = vehicle_class

    @property
    def vin(self):
        """Gets the vin of this VehicleInformation.  # noqa: E501

        the Vehicle Identification Number  # noqa: E501

        :return: The vin of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this VehicleInformation.

        the Vehicle Identification Number  # noqa: E501

        :param vin: The vin of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._vin = vin

    @property
    def year(self):
        """Gets the year of this VehicleInformation.  # noqa: E501

        the model year  # noqa: E501

        :return: The year of this VehicleInformation.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this VehicleInformation.

        the model year  # noqa: E501

        :param year: The year of this VehicleInformation.  # noqa: E501
        :type: str
        """

        self._year = year

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
        if not isinstance(other, VehicleInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
