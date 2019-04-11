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


class QueueConversationCallEventTopicFaxStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationCallEventTopicFaxStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'direction': 'str',
            'expected_pages': 'int',
            'active_page': 'int',
            'lines_transmitted': 'int',
            'bytes_transmitted': 'int',
            'data_rate': 'int',
            'page_errors': 'int',
            'line_errors': 'int'
        }

        self.attribute_map = {
            'direction': 'direction',
            'expected_pages': 'expectedPages',
            'active_page': 'activePage',
            'lines_transmitted': 'linesTransmitted',
            'bytes_transmitted': 'bytesTransmitted',
            'data_rate': 'dataRate',
            'page_errors': 'pageErrors',
            'line_errors': 'lineErrors'
        }

        self._direction = None
        self._expected_pages = None
        self._active_page = None
        self._lines_transmitted = None
        self._bytes_transmitted = None
        self._data_rate = None
        self._page_errors = None
        self._line_errors = None

    @property
    def direction(self):
        """
        Gets the direction of this QueueConversationCallEventTopicFaxStatus.


        :return: The direction of this QueueConversationCallEventTopicFaxStatus.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this QueueConversationCallEventTopicFaxStatus.


        :param direction: The direction of this QueueConversationCallEventTopicFaxStatus.
        :type: str
        """
        
        self._direction = direction

    @property
    def expected_pages(self):
        """
        Gets the expected_pages of this QueueConversationCallEventTopicFaxStatus.


        :return: The expected_pages of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._expected_pages

    @expected_pages.setter
    def expected_pages(self, expected_pages):
        """
        Sets the expected_pages of this QueueConversationCallEventTopicFaxStatus.


        :param expected_pages: The expected_pages of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._expected_pages = expected_pages

    @property
    def active_page(self):
        """
        Gets the active_page of this QueueConversationCallEventTopicFaxStatus.


        :return: The active_page of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._active_page

    @active_page.setter
    def active_page(self, active_page):
        """
        Sets the active_page of this QueueConversationCallEventTopicFaxStatus.


        :param active_page: The active_page of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._active_page = active_page

    @property
    def lines_transmitted(self):
        """
        Gets the lines_transmitted of this QueueConversationCallEventTopicFaxStatus.


        :return: The lines_transmitted of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._lines_transmitted

    @lines_transmitted.setter
    def lines_transmitted(self, lines_transmitted):
        """
        Sets the lines_transmitted of this QueueConversationCallEventTopicFaxStatus.


        :param lines_transmitted: The lines_transmitted of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._lines_transmitted = lines_transmitted

    @property
    def bytes_transmitted(self):
        """
        Gets the bytes_transmitted of this QueueConversationCallEventTopicFaxStatus.


        :return: The bytes_transmitted of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._bytes_transmitted

    @bytes_transmitted.setter
    def bytes_transmitted(self, bytes_transmitted):
        """
        Sets the bytes_transmitted of this QueueConversationCallEventTopicFaxStatus.


        :param bytes_transmitted: The bytes_transmitted of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._bytes_transmitted = bytes_transmitted

    @property
    def data_rate(self):
        """
        Gets the data_rate of this QueueConversationCallEventTopicFaxStatus.


        :return: The data_rate of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._data_rate

    @data_rate.setter
    def data_rate(self, data_rate):
        """
        Sets the data_rate of this QueueConversationCallEventTopicFaxStatus.


        :param data_rate: The data_rate of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._data_rate = data_rate

    @property
    def page_errors(self):
        """
        Gets the page_errors of this QueueConversationCallEventTopicFaxStatus.


        :return: The page_errors of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._page_errors

    @page_errors.setter
    def page_errors(self, page_errors):
        """
        Sets the page_errors of this QueueConversationCallEventTopicFaxStatus.


        :param page_errors: The page_errors of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._page_errors = page_errors

    @property
    def line_errors(self):
        """
        Gets the line_errors of this QueueConversationCallEventTopicFaxStatus.


        :return: The line_errors of this QueueConversationCallEventTopicFaxStatus.
        :rtype: int
        """
        return self._line_errors

    @line_errors.setter
    def line_errors(self, line_errors):
        """
        Sets the line_errors of this QueueConversationCallEventTopicFaxStatus.


        :param line_errors: The line_errors of this QueueConversationCallEventTopicFaxStatus.
        :type: int
        """
        
        self._line_errors = line_errors

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

