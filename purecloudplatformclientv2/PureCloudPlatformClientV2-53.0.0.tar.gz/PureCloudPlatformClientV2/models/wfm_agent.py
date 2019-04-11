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


class WfmAgent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmAgent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user': 'UserReference',
            'work_plan': 'WorkPlanReference',
            'time_zone': 'WfmTimeZone',
            'accept_direct_shift_trades': 'bool',
            'metadata': 'WfmVersionedEntityMetadata',
            'queues': 'list[QueueReference]',
            'languages': 'list[LanguageReference]',
            'skills': 'list[RoutingSkillReference]',
            'schedulable': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'work_plan': 'workPlan',
            'time_zone': 'timeZone',
            'accept_direct_shift_trades': 'acceptDirectShiftTrades',
            'metadata': 'metadata',
            'queues': 'queues',
            'languages': 'languages',
            'skills': 'skills',
            'schedulable': 'schedulable',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._user = None
        self._work_plan = None
        self._time_zone = None
        self._accept_direct_shift_trades = None
        self._metadata = None
        self._queues = None
        self._languages = None
        self._skills = None
        self._schedulable = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this WfmAgent.
        The globally unique identifier for the object.

        :return: The id of this WfmAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WfmAgent.
        The globally unique identifier for the object.

        :param id: The id of this WfmAgent.
        :type: str
        """
        
        self._id = id

    @property
    def user(self):
        """
        Gets the user of this WfmAgent.
        The user associated with this data

        :return: The user of this WfmAgent.
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this WfmAgent.
        The user associated with this data

        :param user: The user of this WfmAgent.
        :type: UserReference
        """
        
        self._user = user

    @property
    def work_plan(self):
        """
        Gets the work_plan of this WfmAgent.
        The work plan associated with this agent

        :return: The work_plan of this WfmAgent.
        :rtype: WorkPlanReference
        """
        return self._work_plan

    @work_plan.setter
    def work_plan(self, work_plan):
        """
        Sets the work_plan of this WfmAgent.
        The work plan associated with this agent

        :param work_plan: The work_plan of this WfmAgent.
        :type: WorkPlanReference
        """
        
        self._work_plan = work_plan

    @property
    def time_zone(self):
        """
        Gets the time_zone of this WfmAgent.
        The time zone for this agent. Defaults to the time zone of the management unit to which the agent belongs

        :return: The time_zone of this WfmAgent.
        :rtype: WfmTimeZone
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this WfmAgent.
        The time zone for this agent. Defaults to the time zone of the management unit to which the agent belongs

        :param time_zone: The time_zone of this WfmAgent.
        :type: WfmTimeZone
        """
        
        self._time_zone = time_zone

    @property
    def accept_direct_shift_trades(self):
        """
        Gets the accept_direct_shift_trades of this WfmAgent.
        Whether the agent accepts direct shift trade requests

        :return: The accept_direct_shift_trades of this WfmAgent.
        :rtype: bool
        """
        return self._accept_direct_shift_trades

    @accept_direct_shift_trades.setter
    def accept_direct_shift_trades(self, accept_direct_shift_trades):
        """
        Sets the accept_direct_shift_trades of this WfmAgent.
        Whether the agent accepts direct shift trade requests

        :param accept_direct_shift_trades: The accept_direct_shift_trades of this WfmAgent.
        :type: bool
        """
        
        self._accept_direct_shift_trades = accept_direct_shift_trades

    @property
    def metadata(self):
        """
        Gets the metadata of this WfmAgent.
        Metadata for this agent

        :return: The metadata of this WfmAgent.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this WfmAgent.
        Metadata for this agent

        :param metadata: The metadata of this WfmAgent.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

    @property
    def queues(self):
        """
        Gets the queues of this WfmAgent.
        List of queues to which the agent belongs and which are defined in the service goal groups in this management unit

        :return: The queues of this WfmAgent.
        :rtype: list[QueueReference]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """
        Sets the queues of this WfmAgent.
        List of queues to which the agent belongs and which are defined in the service goal groups in this management unit

        :param queues: The queues of this WfmAgent.
        :type: list[QueueReference]
        """
        
        self._queues = queues

    @property
    def languages(self):
        """
        Gets the languages of this WfmAgent.
        The list of languages

        :return: The languages of this WfmAgent.
        :rtype: list[LanguageReference]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this WfmAgent.
        The list of languages

        :param languages: The languages of this WfmAgent.
        :type: list[LanguageReference]
        """
        
        self._languages = languages

    @property
    def skills(self):
        """
        Gets the skills of this WfmAgent.
        The list of skills

        :return: The skills of this WfmAgent.
        :rtype: list[RoutingSkillReference]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """
        Sets the skills of this WfmAgent.
        The list of skills

        :param skills: The skills of this WfmAgent.
        :type: list[RoutingSkillReference]
        """
        
        self._skills = skills

    @property
    def schedulable(self):
        """
        Gets the schedulable of this WfmAgent.
        Whether the agent has the permission to be included in schedule generation

        :return: The schedulable of this WfmAgent.
        :rtype: bool
        """
        return self._schedulable

    @schedulable.setter
    def schedulable(self, schedulable):
        """
        Sets the schedulable of this WfmAgent.
        Whether the agent has the permission to be included in schedule generation

        :param schedulable: The schedulable of this WfmAgent.
        :type: bool
        """
        
        self._schedulable = schedulable

    @property
    def self_uri(self):
        """
        Gets the self_uri of this WfmAgent.
        The URI for this object

        :return: The self_uri of this WfmAgent.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this WfmAgent.
        The URI for this object

        :param self_uri: The self_uri of this WfmAgent.
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

