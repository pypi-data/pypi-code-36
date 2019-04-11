# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class DialerContactlistConfigChangeContactList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerContactlistConfigChangeContactList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'column_names': 'list[str]',
            'phone_columns': 'list[DialerContactlistConfigChangeContactPhoneNumberColumn]',
            'import_status': 'DialerContactlistConfigChangeImportStatus',
            'preview_mode_column_name': 'str',
            'preview_mode_accepted_values': 'list[str]',
            'size': 'int',
            'attempt_limits': 'DialerContactlistConfigChangeUriReference',
            'automatic_time_zone_mapping': 'bool',
            'zip_code_column_name': 'str',
            'division': 'DialerContactlistConfigChangeUriReference',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'column_names': 'columnNames',
            'phone_columns': 'phoneColumns',
            'import_status': 'importStatus',
            'preview_mode_column_name': 'previewModeColumnName',
            'preview_mode_accepted_values': 'previewModeAcceptedValues',
            'size': 'size',
            'attempt_limits': 'attemptLimits',
            'automatic_time_zone_mapping': 'automaticTimeZoneMapping',
            'zip_code_column_name': 'zipCodeColumnName',
            'division': 'division',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._column_names = None
        self._phone_columns = None
        self._import_status = None
        self._preview_mode_column_name = None
        self._preview_mode_accepted_values = None
        self._size = None
        self._attempt_limits = None
        self._automatic_time_zone_mapping = None
        self._zip_code_column_name = None
        self._division = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this DialerContactlistConfigChangeContactList.


        :return: The id of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DialerContactlistConfigChangeContactList.


        :param id: The id of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DialerContactlistConfigChangeContactList.


        :return: The name of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DialerContactlistConfigChangeContactList.


        :param name: The name of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this DialerContactlistConfigChangeContactList.


        :return: The date_created of this DialerContactlistConfigChangeContactList.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this DialerContactlistConfigChangeContactList.


        :param date_created: The date_created of this DialerContactlistConfigChangeContactList.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this DialerContactlistConfigChangeContactList.


        :return: The date_modified of this DialerContactlistConfigChangeContactList.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this DialerContactlistConfigChangeContactList.


        :param date_modified: The date_modified of this DialerContactlistConfigChangeContactList.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this DialerContactlistConfigChangeContactList.


        :return: The version of this DialerContactlistConfigChangeContactList.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DialerContactlistConfigChangeContactList.


        :param version: The version of this DialerContactlistConfigChangeContactList.
        :type: int
        """
        
        self._version = version

    @property
    def column_names(self):
        """
        Gets the column_names of this DialerContactlistConfigChangeContactList.


        :return: The column_names of this DialerContactlistConfigChangeContactList.
        :rtype: list[str]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """
        Sets the column_names of this DialerContactlistConfigChangeContactList.


        :param column_names: The column_names of this DialerContactlistConfigChangeContactList.
        :type: list[str]
        """
        
        self._column_names = column_names

    @property
    def phone_columns(self):
        """
        Gets the phone_columns of this DialerContactlistConfigChangeContactList.


        :return: The phone_columns of this DialerContactlistConfigChangeContactList.
        :rtype: list[DialerContactlistConfigChangeContactPhoneNumberColumn]
        """
        return self._phone_columns

    @phone_columns.setter
    def phone_columns(self, phone_columns):
        """
        Sets the phone_columns of this DialerContactlistConfigChangeContactList.


        :param phone_columns: The phone_columns of this DialerContactlistConfigChangeContactList.
        :type: list[DialerContactlistConfigChangeContactPhoneNumberColumn]
        """
        
        self._phone_columns = phone_columns

    @property
    def import_status(self):
        """
        Gets the import_status of this DialerContactlistConfigChangeContactList.


        :return: The import_status of this DialerContactlistConfigChangeContactList.
        :rtype: DialerContactlistConfigChangeImportStatus
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        """
        Sets the import_status of this DialerContactlistConfigChangeContactList.


        :param import_status: The import_status of this DialerContactlistConfigChangeContactList.
        :type: DialerContactlistConfigChangeImportStatus
        """
        
        self._import_status = import_status

    @property
    def preview_mode_column_name(self):
        """
        Gets the preview_mode_column_name of this DialerContactlistConfigChangeContactList.


        :return: The preview_mode_column_name of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._preview_mode_column_name

    @preview_mode_column_name.setter
    def preview_mode_column_name(self, preview_mode_column_name):
        """
        Sets the preview_mode_column_name of this DialerContactlistConfigChangeContactList.


        :param preview_mode_column_name: The preview_mode_column_name of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        
        self._preview_mode_column_name = preview_mode_column_name

    @property
    def preview_mode_accepted_values(self):
        """
        Gets the preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.


        :return: The preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.
        :rtype: list[str]
        """
        return self._preview_mode_accepted_values

    @preview_mode_accepted_values.setter
    def preview_mode_accepted_values(self, preview_mode_accepted_values):
        """
        Sets the preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.


        :param preview_mode_accepted_values: The preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.
        :type: list[str]
        """
        
        self._preview_mode_accepted_values = preview_mode_accepted_values

    @property
    def size(self):
        """
        Gets the size of this DialerContactlistConfigChangeContactList.


        :return: The size of this DialerContactlistConfigChangeContactList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this DialerContactlistConfigChangeContactList.


        :param size: The size of this DialerContactlistConfigChangeContactList.
        :type: int
        """
        
        self._size = size

    @property
    def attempt_limits(self):
        """
        Gets the attempt_limits of this DialerContactlistConfigChangeContactList.


        :return: The attempt_limits of this DialerContactlistConfigChangeContactList.
        :rtype: DialerContactlistConfigChangeUriReference
        """
        return self._attempt_limits

    @attempt_limits.setter
    def attempt_limits(self, attempt_limits):
        """
        Sets the attempt_limits of this DialerContactlistConfigChangeContactList.


        :param attempt_limits: The attempt_limits of this DialerContactlistConfigChangeContactList.
        :type: DialerContactlistConfigChangeUriReference
        """
        
        self._attempt_limits = attempt_limits

    @property
    def automatic_time_zone_mapping(self):
        """
        Gets the automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.


        :return: The automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.
        :rtype: bool
        """
        return self._automatic_time_zone_mapping

    @automatic_time_zone_mapping.setter
    def automatic_time_zone_mapping(self, automatic_time_zone_mapping):
        """
        Sets the automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.


        :param automatic_time_zone_mapping: The automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.
        :type: bool
        """
        
        self._automatic_time_zone_mapping = automatic_time_zone_mapping

    @property
    def zip_code_column_name(self):
        """
        Gets the zip_code_column_name of this DialerContactlistConfigChangeContactList.


        :return: The zip_code_column_name of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._zip_code_column_name

    @zip_code_column_name.setter
    def zip_code_column_name(self, zip_code_column_name):
        """
        Sets the zip_code_column_name of this DialerContactlistConfigChangeContactList.


        :param zip_code_column_name: The zip_code_column_name of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        
        self._zip_code_column_name = zip_code_column_name

    @property
    def division(self):
        """
        Gets the division of this DialerContactlistConfigChangeContactList.


        :return: The division of this DialerContactlistConfigChangeContactList.
        :rtype: DialerContactlistConfigChangeUriReference
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this DialerContactlistConfigChangeContactList.


        :param division: The division of this DialerContactlistConfigChangeContactList.
        :type: DialerContactlistConfigChangeUriReference
        """
        
        self._division = division

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DialerContactlistConfigChangeContactList.


        :return: The additional_properties of this DialerContactlistConfigChangeContactList.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DialerContactlistConfigChangeContactList.


        :param additional_properties: The additional_properties of this DialerContactlistConfigChangeContactList.
        :type: object
        """
        
        self._additional_properties = additional_properties

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

