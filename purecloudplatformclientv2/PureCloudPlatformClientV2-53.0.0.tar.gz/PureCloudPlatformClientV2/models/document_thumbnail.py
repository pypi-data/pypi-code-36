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


class DocumentThumbnail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DocumentThumbnail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'resolution': 'str',
            'image_uri': 'str',
            'height': 'int',
            'width': 'int'
        }

        self.attribute_map = {
            'resolution': 'resolution',
            'image_uri': 'imageUri',
            'height': 'height',
            'width': 'width'
        }

        self._resolution = None
        self._image_uri = None
        self._height = None
        self._width = None

    @property
    def resolution(self):
        """
        Gets the resolution of this DocumentThumbnail.


        :return: The resolution of this DocumentThumbnail.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this DocumentThumbnail.


        :param resolution: The resolution of this DocumentThumbnail.
        :type: str
        """
        
        self._resolution = resolution

    @property
    def image_uri(self):
        """
        Gets the image_uri of this DocumentThumbnail.


        :return: The image_uri of this DocumentThumbnail.
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """
        Sets the image_uri of this DocumentThumbnail.


        :param image_uri: The image_uri of this DocumentThumbnail.
        :type: str
        """
        
        self._image_uri = image_uri

    @property
    def height(self):
        """
        Gets the height of this DocumentThumbnail.


        :return: The height of this DocumentThumbnail.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this DocumentThumbnail.


        :param height: The height of this DocumentThumbnail.
        :type: int
        """
        
        self._height = height

    @property
    def width(self):
        """
        Gets the width of this DocumentThumbnail.


        :return: The width of this DocumentThumbnail.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this DocumentThumbnail.


        :param width: The width of this DocumentThumbnail.
        :type: int
        """
        
        self._width = width

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

