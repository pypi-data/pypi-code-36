# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.4
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AlertWatcherTest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'accepted': 'bool',
        'error': 'str'
    }

    attribute_map = {
        'name': 'name',
        'accepted': 'accepted',
        'error': 'error'
    }

    def __init__(self, name=None, accepted=None, error=None):
        """
        AlertWatcherTest - a model defined in Swagger
        """

        self._name = None
        self._accepted = None
        self._error = None

        if name is not None:
          self.name = name
        if accepted is not None:
          self.accepted = accepted
        if error is not None:
          self.error = error

    @property
    def name(self):
        """
        Gets the name of this AlertWatcherTest.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this AlertWatcherTest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AlertWatcherTest.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this AlertWatcherTest.
        :type: str
        """

        self._name = name

    @property
    def accepted(self):
        """
        Gets the accepted of this AlertWatcherTest.
        is the email accepted?

        :return: The accepted of this AlertWatcherTest.
        :rtype: bool
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """
        Sets the accepted of this AlertWatcherTest.
        is the email accepted?

        :param accepted: The accepted of this AlertWatcherTest.
        :type: bool
        """

        self._accepted = accepted

    @property
    def error(self):
        """
        Gets the error of this AlertWatcherTest.
        error message (if failed)

        :return: The error of this AlertWatcherTest.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this AlertWatcherTest.
        error message (if failed)

        :param error: The error of this AlertWatcherTest.
        :type: str
        """

        self._error = error

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AlertWatcherTest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
