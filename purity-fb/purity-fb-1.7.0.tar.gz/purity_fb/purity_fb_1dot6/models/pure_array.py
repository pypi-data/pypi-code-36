# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.6), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PureArray(object):
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
        'id': 'str',
        'ntp_servers': 'list[str]',
        'os': 'str',
        'version': 'str',
        'revision': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'ntp_servers': 'ntp_servers',
        'os': 'os',
        'version': 'version',
        'revision': 'revision'
    }

    def __init__(self, name=None, id=None, ntp_servers=None, os=None, version=None, revision=None):
        """
        PureArray - a model defined in Swagger
        """

        self._name = None
        self._id = None
        self._ntp_servers = None
        self._os = None
        self._version = None
        self._revision = None

        if name is not None:
          self.name = name
        if id is not None:
          self.id = id
        if ntp_servers is not None:
          self.ntp_servers = ntp_servers
        if os is not None:
          self.os = os
        if version is not None:
          self.version = version
        if revision is not None:
          self.revision = revision

    @property
    def name(self):
        """
        Gets the name of this PureArray.
        name of the object

        :return: The name of this PureArray.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PureArray.
        name of the object

        :param name: The name of this PureArray.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this PureArray.
        A globally unique ID chosen by the system. Cannot change. Cannot ever refer to another resource.

        :return: The id of this PureArray.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PureArray.
        A globally unique ID chosen by the system. Cannot change. Cannot ever refer to another resource.

        :param id: The id of this PureArray.
        :type: str
        """

        self._id = id

    @property
    def ntp_servers(self):
        """
        Gets the ntp_servers of this PureArray.

        :return: The ntp_servers of this PureArray.
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """
        Sets the ntp_servers of this PureArray.

        :param ntp_servers: The ntp_servers of this PureArray.
        :type: list[str]
        """

        self._ntp_servers = ntp_servers

    @property
    def os(self):
        """
        Gets the os of this PureArray.
        Possible values are Purity//FA and Purity//FB.

        :return: The os of this PureArray.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this PureArray.
        Possible values are Purity//FA and Purity//FB.

        :param os: The os of this PureArray.
        :type: str
        """

        self._os = os

    @property
    def version(self):
        """
        Gets the version of this PureArray.

        :return: The version of this PureArray.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PureArray.

        :param version: The version of this PureArray.
        :type: str
        """

        self._version = version

    @property
    def revision(self):
        """
        Gets the revision of this PureArray.

        :return: The revision of this PureArray.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this PureArray.

        :param revision: The revision of this PureArray.
        :type: str
        """

        self._revision = revision

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
        if not isinstance(other, PureArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
