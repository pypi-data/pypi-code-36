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


class UserPresence(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserPresence - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'source': 'str',
            'primary': 'bool',
            'presence_definition': 'PresenceDefinition',
            'message': 'str',
            'modified_date': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'source': 'source',
            'primary': 'primary',
            'presence_definition': 'presenceDefinition',
            'message': 'message',
            'modified_date': 'modifiedDate',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._source = None
        self._primary = None
        self._presence_definition = None
        self._message = None
        self._modified_date = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this UserPresence.
        The globally unique identifier for the object.

        :return: The id of this UserPresence.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserPresence.
        The globally unique identifier for the object.

        :param id: The id of this UserPresence.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UserPresence.


        :return: The name of this UserPresence.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserPresence.


        :param name: The name of this UserPresence.
        :type: str
        """
        
        self._name = name

    @property
    def source(self):
        """
        Gets the source of this UserPresence.
        Represents the source where the Presence was set. Some examples are: PURECLOUD, LYNC, OUTLOOK, etc.

        :return: The source of this UserPresence.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this UserPresence.
        Represents the source where the Presence was set. Some examples are: PURECLOUD, LYNC, OUTLOOK, etc.

        :param source: The source of this UserPresence.
        :type: str
        """
        
        self._source = source

    @property
    def primary(self):
        """
        Gets the primary of this UserPresence.
        A boolean used to tell whether or not to set this presence source as the primary on a PATCH

        :return: The primary of this UserPresence.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """
        Sets the primary of this UserPresence.
        A boolean used to tell whether or not to set this presence source as the primary on a PATCH

        :param primary: The primary of this UserPresence.
        :type: bool
        """
        
        self._primary = primary

    @property
    def presence_definition(self):
        """
        Gets the presence_definition of this UserPresence.


        :return: The presence_definition of this UserPresence.
        :rtype: PresenceDefinition
        """
        return self._presence_definition

    @presence_definition.setter
    def presence_definition(self, presence_definition):
        """
        Sets the presence_definition of this UserPresence.


        :param presence_definition: The presence_definition of this UserPresence.
        :type: PresenceDefinition
        """
        
        self._presence_definition = presence_definition

    @property
    def message(self):
        """
        Gets the message of this UserPresence.


        :return: The message of this UserPresence.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this UserPresence.


        :param message: The message of this UserPresence.
        :type: str
        """
        
        self._message = message

    @property
    def modified_date(self):
        """
        Gets the modified_date of this UserPresence.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The modified_date of this UserPresence.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this UserPresence.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param modified_date: The modified_date of this UserPresence.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def self_uri(self):
        """
        Gets the self_uri of this UserPresence.
        The URI for this object

        :return: The self_uri of this UserPresence.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this UserPresence.
        The URI for this object

        :param self_uri: The self_uri of this UserPresence.
        :type: str
        """
        
        self._self_uri = self_uri

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

