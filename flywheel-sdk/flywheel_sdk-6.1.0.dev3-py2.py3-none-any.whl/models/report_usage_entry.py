# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1.0-dev.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.report_usage_project_entry import ReportUsageProjectEntry  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class ReportUsageEntry(object):

    swagger_types = {
        'file_mbs': 'float',
        'gear_execution_count': 'int',
        'session_count': 'int',
        'year': 'str',
        'month': 'str',
        'project': 'ReportUsageProjectEntry'
    }

    attribute_map = {
        'file_mbs': 'file_mbs',
        'gear_execution_count': 'gear_execution_count',
        'session_count': 'session_count',
        'year': 'year',
        'month': 'month',
        'project': 'project'
    }

    rattribute_map = {
        'file_mbs': 'file_mbs',
        'gear_execution_count': 'gear_execution_count',
        'session_count': 'session_count',
        'year': 'year',
        'month': 'month',
        'project': 'project'
    }

    def __init__(self, file_mbs=None, gear_execution_count=None, session_count=None, year=None, month=None, project=None):  # noqa: E501
        """ReportUsageEntry - a model defined in Swagger"""
        super(ReportUsageEntry, self).__init__()

        self._file_mbs = None
        self._gear_execution_count = None
        self._session_count = None
        self._year = None
        self._month = None
        self._project = None
        self.discriminator = None
        self.alt_discriminator = None

        self.file_mbs = file_mbs
        self.gear_execution_count = gear_execution_count
        self.session_count = session_count
        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if project is not None:
            self.project = project

    @property
    def file_mbs(self):
        """Gets the file_mbs of this ReportUsageEntry.

        File storage usage, in megabytes

        :return: The file_mbs of this ReportUsageEntry.
        :rtype: float
        """
        return self._file_mbs

    @file_mbs.setter
    def file_mbs(self, file_mbs):
        """Sets the file_mbs of this ReportUsageEntry.

        File storage usage, in megabytes

        :param file_mbs: The file_mbs of this ReportUsageEntry.  # noqa: E501
        :type: float
        """

        self._file_mbs = file_mbs

    @property
    def gear_execution_count(self):
        """Gets the gear_execution_count of this ReportUsageEntry.

        The number of gears executed

        :return: The gear_execution_count of this ReportUsageEntry.
        :rtype: int
        """
        return self._gear_execution_count

    @gear_execution_count.setter
    def gear_execution_count(self, gear_execution_count):
        """Sets the gear_execution_count of this ReportUsageEntry.

        The number of gears executed

        :param gear_execution_count: The gear_execution_count of this ReportUsageEntry.  # noqa: E501
        :type: int
        """

        self._gear_execution_count = gear_execution_count

    @property
    def session_count(self):
        """Gets the session_count of this ReportUsageEntry.

        The number of sessions created

        :return: The session_count of this ReportUsageEntry.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        """Sets the session_count of this ReportUsageEntry.

        The number of sessions created

        :param session_count: The session_count of this ReportUsageEntry.  # noqa: E501
        :type: int
        """

        self._session_count = session_count

    @property
    def year(self):
        """Gets the year of this ReportUsageEntry.

        The year portion of the entry date

        :return: The year of this ReportUsageEntry.
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ReportUsageEntry.

        The year portion of the entry date

        :param year: The year of this ReportUsageEntry.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def month(self):
        """Gets the month of this ReportUsageEntry.

        The month portion of the entry date

        :return: The month of this ReportUsageEntry.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ReportUsageEntry.

        The month portion of the entry date

        :param month: The month of this ReportUsageEntry.  # noqa: E501
        :type: str
        """

        self._month = month

    @property
    def project(self):
        """Gets the project of this ReportUsageEntry.


        :return: The project of this ReportUsageEntry.
        :rtype: ReportUsageProjectEntry
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ReportUsageEntry.


        :param project: The project of this ReportUsageEntry.  # noqa: E501
        :type: ReportUsageProjectEntry
        """

        self._project = project


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

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
        if not isinstance(other, ReportUsageEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
