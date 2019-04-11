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


class ConversationEventTopicConversation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationEventTopicConversation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'max_participants': 'int',
            'participants': 'list[ConversationEventTopicParticipant]',
            'recording_state': 'str',
            'address': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'max_participants': 'maxParticipants',
            'participants': 'participants',
            'recording_state': 'recordingState',
            'address': 'address'
        }

        self._id = None
        self._max_participants = None
        self._participants = None
        self._recording_state = None
        self._address = None

    @property
    def id(self):
        """
        Gets the id of this ConversationEventTopicConversation.


        :return: The id of this ConversationEventTopicConversation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConversationEventTopicConversation.


        :param id: The id of this ConversationEventTopicConversation.
        :type: str
        """
        
        self._id = id

    @property
    def max_participants(self):
        """
        Gets the max_participants of this ConversationEventTopicConversation.


        :return: The max_participants of this ConversationEventTopicConversation.
        :rtype: int
        """
        return self._max_participants

    @max_participants.setter
    def max_participants(self, max_participants):
        """
        Sets the max_participants of this ConversationEventTopicConversation.


        :param max_participants: The max_participants of this ConversationEventTopicConversation.
        :type: int
        """
        
        self._max_participants = max_participants

    @property
    def participants(self):
        """
        Gets the participants of this ConversationEventTopicConversation.


        :return: The participants of this ConversationEventTopicConversation.
        :rtype: list[ConversationEventTopicParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """
        Sets the participants of this ConversationEventTopicConversation.


        :param participants: The participants of this ConversationEventTopicConversation.
        :type: list[ConversationEventTopicParticipant]
        """
        
        self._participants = participants

    @property
    def recording_state(self):
        """
        Gets the recording_state of this ConversationEventTopicConversation.


        :return: The recording_state of this ConversationEventTopicConversation.
        :rtype: str
        """
        return self._recording_state

    @recording_state.setter
    def recording_state(self, recording_state):
        """
        Sets the recording_state of this ConversationEventTopicConversation.


        :param recording_state: The recording_state of this ConversationEventTopicConversation.
        :type: str
        """
        
        self._recording_state = recording_state

    @property
    def address(self):
        """
        Gets the address of this ConversationEventTopicConversation.


        :return: The address of this ConversationEventTopicConversation.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ConversationEventTopicConversation.


        :param address: The address of this ConversationEventTopicConversation.
        :type: str
        """
        
        self._address = address

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

