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


class QuotasGroup(object):
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
        'file_system': 'FixedReference',
        'file_system_default_quota': 'int',
        'group': 'QuotasgroupGroup',
        'quota': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'name': 'name',
        'file_system': 'file_system',
        'file_system_default_quota': 'file_system_default_quota',
        'group': 'group',
        'quota': 'quota',
        'usage': 'usage'
    }

    def __init__(self, name=None, file_system=None, file_system_default_quota=None, group=None, quota=None, usage=None):
        """
        QuotasGroup - a model defined in Swagger
        """

        self._name = None
        self._file_system = None
        self._file_system_default_quota = None
        self._group = None
        self._quota = None
        self._usage = None

        if name is not None:
          self.name = name
        if file_system is not None:
          self.file_system = file_system
        if file_system_default_quota is not None:
          self.file_system_default_quota = file_system_default_quota
        if group is not None:
          self.group = group
        if quota is not None:
          self.quota = quota
        if usage is not None:
          self.usage = usage

    @property
    def name(self):
        """
        Gets the name of this QuotasGroup.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this QuotasGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QuotasGroup.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this QuotasGroup.
        :type: str
        """

        self._name = name

    @property
    def file_system(self):
        """
        Gets the file_system of this QuotasGroup.

        :return: The file_system of this QuotasGroup.
        :rtype: FixedReference
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """
        Sets the file_system of this QuotasGroup.

        :param file_system: The file_system of this QuotasGroup.
        :type: FixedReference
        """

        self._file_system = file_system

    @property
    def file_system_default_quota(self):
        """
        Gets the file_system_default_quota of this QuotasGroup.
        File system's default group quota (in bytes). If it is 0, it means there is no default quota. This will be the effective group quota if the group doesn't have an individual quota. This default quota is set through the file-system endpoint.

        :return: The file_system_default_quota of this QuotasGroup.
        :rtype: int
        """
        return self._file_system_default_quota

    @file_system_default_quota.setter
    def file_system_default_quota(self, file_system_default_quota):
        """
        Sets the file_system_default_quota of this QuotasGroup.
        File system's default group quota (in bytes). If it is 0, it means there is no default quota. This will be the effective group quota if the group doesn't have an individual quota. This default quota is set through the file-system endpoint.

        :param file_system_default_quota: The file_system_default_quota of this QuotasGroup.
        :type: int
        """

        self._file_system_default_quota = file_system_default_quota

    @property
    def group(self):
        """
        Gets the group of this QuotasGroup.

        :return: The group of this QuotasGroup.
        :rtype: QuotasgroupGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this QuotasGroup.

        :param group: The group of this QuotasGroup.
        :type: QuotasgroupGroup
        """

        self._group = group

    @property
    def quota(self):
        """
        Gets the quota of this QuotasGroup.
        The space limit of the quota (in bytes) for the specified group, cannot be 0. Modifiable. If specified, this value will override the file system's default group quota.

        :return: The quota of this QuotasGroup.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """
        Sets the quota of this QuotasGroup.
        The space limit of the quota (in bytes) for the specified group, cannot be 0. Modifiable. If specified, this value will override the file system's default group quota.

        :param quota: The quota of this QuotasGroup.
        :type: int
        """

        self._quota = quota

    @property
    def usage(self):
        """
        Gets the usage of this QuotasGroup.
        The usage of the file system (in bytes) by the specified group.

        :return: The usage of this QuotasGroup.
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this QuotasGroup.
        The usage of the file system (in bytes) by the specified group.

        :param usage: The usage of this QuotasGroup.
        :type: int
        """

        self._usage = usage

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
        if not isinstance(other, QuotasGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
