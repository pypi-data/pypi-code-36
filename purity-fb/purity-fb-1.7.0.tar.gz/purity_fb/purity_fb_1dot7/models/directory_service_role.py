# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.7), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.7
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DirectoryServiceRole(object):
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
        'group': 'str',
        'group_base': 'str'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'group_base': 'group_base'
    }

    def __init__(self, name=None, group=None, group_base=None):
        """
        DirectoryServiceRole - a model defined in Swagger
        """

        self._name = None
        self._group = None
        self._group_base = None

        if name is not None:
          self.name = name
        if group is not None:
          self.group = group
        if group_base is not None:
          self.group_base = group_base

    @property
    def name(self):
        """
        Gets the name of this DirectoryServiceRole.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this DirectoryServiceRole.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DirectoryServiceRole.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this DirectoryServiceRole.
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """
        Gets the group of this DirectoryServiceRole.
        Common Name (CN) of the directory service group containing administrators with full privileges to manage the array

        :return: The group of this DirectoryServiceRole.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this DirectoryServiceRole.
        Common Name (CN) of the directory service group containing administrators with full privileges to manage the array

        :param group: The group of this DirectoryServiceRole.
        :type: str
        """

        self._group = group

    @property
    def group_base(self):
        """
        Gets the group_base of this DirectoryServiceRole.
        Specifies where the configured groups are located in the directory tree

        :return: The group_base of this DirectoryServiceRole.
        :rtype: str
        """
        return self._group_base

    @group_base.setter
    def group_base(self, group_base):
        """
        Sets the group_base of this DirectoryServiceRole.
        Specifies where the configured groups are located in the directory tree

        :param group_base: The group_base of this DirectoryServiceRole.
        :type: str
        """

        self._group_base = group_base

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
        if not isinstance(other, DirectoryServiceRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
