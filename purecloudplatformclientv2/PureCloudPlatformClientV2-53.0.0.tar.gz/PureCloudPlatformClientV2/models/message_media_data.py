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


class MessageMediaData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessageMediaData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'url': 'str',
            'media_type': 'str',
            'content_length_bytes': 'int',
            'upload_url': 'str',
            'status': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'url': 'url',
            'media_type': 'mediaType',
            'content_length_bytes': 'contentLengthBytes',
            'upload_url': 'uploadUrl',
            'status': 'status',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._url = None
        self._media_type = None
        self._content_length_bytes = None
        self._upload_url = None
        self._status = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this MessageMediaData.
        The globally unique identifier for the object.

        :return: The id of this MessageMediaData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MessageMediaData.
        The globally unique identifier for the object.

        :param id: The id of this MessageMediaData.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MessageMediaData.


        :return: The name of this MessageMediaData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessageMediaData.


        :param name: The name of this MessageMediaData.
        :type: str
        """
        
        self._name = name

    @property
    def url(self):
        """
        Gets the url of this MessageMediaData.
        The location of the media, useful for retrieving it

        :return: The url of this MessageMediaData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this MessageMediaData.
        The location of the media, useful for retrieving it

        :param url: The url of this MessageMediaData.
        :type: str
        """
        
        self._url = url

    @property
    def media_type(self):
        """
        Gets the media_type of this MessageMediaData.
        The optional internet media type of the the media object.  If null then the media type should be dictated by the url.

        :return: The media_type of this MessageMediaData.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this MessageMediaData.
        The optional internet media type of the the media object.  If null then the media type should be dictated by the url.

        :param media_type: The media_type of this MessageMediaData.
        :type: str
        """
        allowed_values = ["image/png", "image/jpeg", "image/gif"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for media_type -> " + media_type
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def content_length_bytes(self):
        """
        Gets the content_length_bytes of this MessageMediaData.
        The optional content length of the the media object, in bytes.

        :return: The content_length_bytes of this MessageMediaData.
        :rtype: int
        """
        return self._content_length_bytes

    @content_length_bytes.setter
    def content_length_bytes(self, content_length_bytes):
        """
        Sets the content_length_bytes of this MessageMediaData.
        The optional content length of the the media object, in bytes.

        :param content_length_bytes: The content_length_bytes of this MessageMediaData.
        :type: int
        """
        
        self._content_length_bytes = content_length_bytes

    @property
    def upload_url(self):
        """
        Gets the upload_url of this MessageMediaData.
        The URL returned to upload an attachment

        :return: The upload_url of this MessageMediaData.
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """
        Sets the upload_url of this MessageMediaData.
        The URL returned to upload an attachment

        :param upload_url: The upload_url of this MessageMediaData.
        :type: str
        """
        
        self._upload_url = upload_url

    @property
    def status(self):
        """
        Gets the status of this MessageMediaData.
        The status of the media, indicates if the media is in the process of uploading. If the upload fails, the media becomes invalid

        :return: The status of this MessageMediaData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MessageMediaData.
        The status of the media, indicates if the media is in the process of uploading. If the upload fails, the media becomes invalid

        :param status: The status of this MessageMediaData.
        :type: str
        """
        allowed_values = ["uploading", "valid", "invalid"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def self_uri(self):
        """
        Gets the self_uri of this MessageMediaData.
        The URI for this object

        :return: The self_uri of this MessageMediaData.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this MessageMediaData.
        The URI for this object

        :param self_uri: The self_uri of this MessageMediaData.
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

