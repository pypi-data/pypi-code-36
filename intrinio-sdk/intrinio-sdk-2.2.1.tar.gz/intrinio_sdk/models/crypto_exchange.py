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


class CryptoExchange(object):
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
        'name': 'str',
        'code': 'str',
        'book_depth_available': 'bool',
        'history_available': 'bool',
        'snapshot_available': 'bool',
        'trades_available': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'book_depth_available': 'book_depth_available',
        'history_available': 'history_available',
        'snapshot_available': 'snapshot_available',
        'trades_available': 'trades_available'
    }

    def __init__(self, name=None, code=None, book_depth_available=None, history_available=None, snapshot_available=None, trades_available=None):  # noqa: E501
        """CryptoExchange - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._code = None
        self._book_depth_available = None
        self._history_available = None
        self._snapshot_available = None
        self._trades_available = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if book_depth_available is not None:
            self.book_depth_available = book_depth_available
        if history_available is not None:
            self.history_available = history_available
        if snapshot_available is not None:
            self.snapshot_available = snapshot_available
        if trades_available is not None:
            self.trades_available = trades_available

    @property
    def name(self):
        """Gets the name of this CryptoExchange.  # noqa: E501

        The Crypto Exchange name.  # noqa: E501

        :return: The name of this CryptoExchange.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this CryptoExchange.  # noqa: E501

        The Crypto Exchange name. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this CryptoExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
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
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this CryptoExchange.

        The Crypto Exchange name.  # noqa: E501

        :param name: The name of this CryptoExchange.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this CryptoExchange.  # noqa: E501

        The Crypto Exchange code.  # noqa: E501

        :return: The code of this CryptoExchange.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this CryptoExchange.  # noqa: E501

        The Crypto Exchange code. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this CryptoExchange.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.code
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
            result = { 'code': value }

        
        return result
        

    @code.setter
    def code(self, code):
        """Sets the code of this CryptoExchange.

        The Crypto Exchange code.  # noqa: E501

        :param code: The code of this CryptoExchange.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def book_depth_available(self):
        """Gets the book_depth_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether book depth data is provided by this exchange or not.  # noqa: E501

        :return: The book_depth_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """
        return self._book_depth_available
        
    @property
    def book_depth_available_dict(self):
        """Gets the book_depth_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether book depth data is provided by this exchange or not. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The book_depth_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.book_depth_available
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
            result = { 'book_depth_available': value }

        
        return result
        

    @book_depth_available.setter
    def book_depth_available(self, book_depth_available):
        """Sets the book_depth_available of this CryptoExchange.

        A boolean, representing whether book depth data is provided by this exchange or not.  # noqa: E501

        :param book_depth_available: The book_depth_available of this CryptoExchange.  # noqa: E501
        :type: bool
        """

        self._book_depth_available = book_depth_available

    @property
    def history_available(self):
        """Gets the history_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether historical data is provided by this exchange or not.  # noqa: E501

        :return: The history_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """
        return self._history_available
        
    @property
    def history_available_dict(self):
        """Gets the history_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether historical data is provided by this exchange or not. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The history_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.history_available
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
            result = { 'history_available': value }

        
        return result
        

    @history_available.setter
    def history_available(self, history_available):
        """Sets the history_available of this CryptoExchange.

        A boolean, representing whether historical data is provided by this exchange or not.  # noqa: E501

        :param history_available: The history_available of this CryptoExchange.  # noqa: E501
        :type: bool
        """

        self._history_available = history_available

    @property
    def snapshot_available(self):
        """Gets the snapshot_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether snpashot data is provided by this exchange or not.  # noqa: E501

        :return: The snapshot_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """
        return self._snapshot_available
        
    @property
    def snapshot_available_dict(self):
        """Gets the snapshot_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether snpashot data is provided by this exchange or not. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The snapshot_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.snapshot_available
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
            result = { 'snapshot_available': value }

        
        return result
        

    @snapshot_available.setter
    def snapshot_available(self, snapshot_available):
        """Sets the snapshot_available of this CryptoExchange.

        A boolean, representing whether snpashot data is provided by this exchange or not.  # noqa: E501

        :param snapshot_available: The snapshot_available of this CryptoExchange.  # noqa: E501
        :type: bool
        """

        self._snapshot_available = snapshot_available

    @property
    def trades_available(self):
        """Gets the trades_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether trade data is provided by this exchange or not.  # noqa: E501

        :return: The trades_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """
        return self._trades_available
        
    @property
    def trades_available_dict(self):
        """Gets the trades_available of this CryptoExchange.  # noqa: E501

        A boolean, representing whether trade data is provided by this exchange or not. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The trades_available of this CryptoExchange.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.trades_available
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
            result = { 'trades_available': value }

        
        return result
        

    @trades_available.setter
    def trades_available(self, trades_available):
        """Sets the trades_available of this CryptoExchange.

        A boolean, representing whether trade data is provided by this exchange or not.  # noqa: E501

        :param trades_available: The trades_available of this CryptoExchange.  # noqa: E501
        :type: bool
        """

        self._trades_available = trades_available

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
        if not isinstance(other, CryptoExchange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
