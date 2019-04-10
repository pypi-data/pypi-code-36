# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.96
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ClientLogEntry(object):
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
        'logger': 'str',
        'message': 'str',
        'level': 'str',
        'timestamp': 'int',
        'url': 'str'
    }

    attribute_map = {
        'logger': 'logger',
        'message': 'message',
        'level': 'level',
        'timestamp': 'timestamp',
        'url': 'url'
    }

    def __init__(self, logger=None, message=None, level=None, timestamp=None, url=None):  # noqa: E501
        """ClientLogEntry - a model defined in OpenAPI"""  # noqa: E501

        self._logger = None
        self._message = None
        self._level = None
        self._timestamp = None
        self._url = None
        self.discriminator = None

        if logger is not None:
            self.logger = logger
        if message is not None:
            self.message = message
        if level is not None:
            self.level = level
        if timestamp is not None:
            self.timestamp = timestamp
        if url is not None:
            self.url = url

    @property
    def logger(self):
        """Gets the logger of this ClientLogEntry.  # noqa: E501


        :return: The logger of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._logger

    @logger.setter
    def logger(self, logger):
        """Sets the logger of this ClientLogEntry.


        :param logger: The logger of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._logger = logger

    @property
    def message(self):
        """Gets the message of this ClientLogEntry.  # noqa: E501


        :return: The message of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ClientLogEntry.


        :param message: The message of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def level(self):
        """Gets the level of this ClientLogEntry.  # noqa: E501


        :return: The level of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ClientLogEntry.


        :param level: The level of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def timestamp(self):
        """Gets the timestamp of this ClientLogEntry.  # noqa: E501


        :return: The timestamp of this ClientLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ClientLogEntry.


        :param timestamp: The timestamp of this ClientLogEntry.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def url(self):
        """Gets the url of this ClientLogEntry.  # noqa: E501


        :return: The url of this ClientLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ClientLogEntry.


        :param url: The url of this ClientLogEntry.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, ClientLogEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
