# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PublicTableDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'headers': 'list[Header]',
        'id': 'str',
        'image': 'PublicTableImageDto',
        'name': 'str',
        'orientation': 'str',
        'values': 'list[Cells]'
    }

    attribute_map = {
        'headers': 'headers',
        'id': 'id',
        'image': 'image',
        'name': 'name',
        'orientation': 'orientation',
        'values': 'values'
    }

    def __init__(self, headers=None, id=None, image=None, name=None, orientation=None, values=None):  # noqa: E501
        """PublicTableDto - a model defined in OpenAPI"""  # noqa: E501

        self._headers = None
        self._id = None
        self._image = None
        self._name = None
        self._orientation = None
        self._values = None
        self.discriminator = None

        self.headers = headers
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        self.name = name
        self.orientation = orientation
        self.values = values

    @property
    def headers(self):
        """Gets the headers of this PublicTableDto.  # noqa: E501


        :return: The headers of this PublicTableDto.  # noqa: E501
        :rtype: list[Header]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this PublicTableDto.


        :param headers: The headers of this PublicTableDto.  # noqa: E501
        :type: list[Header]
        """
        if headers is None:
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

    @property
    def id(self):
        """Gets the id of this PublicTableDto.  # noqa: E501


        :return: The id of this PublicTableDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicTableDto.


        :param id: The id of this PublicTableDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this PublicTableDto.  # noqa: E501


        :return: The image of this PublicTableDto.  # noqa: E501
        :rtype: PublicTableImageDto
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PublicTableDto.


        :param image: The image of this PublicTableDto.  # noqa: E501
        :type: PublicTableImageDto
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this PublicTableDto.  # noqa: E501


        :return: The name of this PublicTableDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicTableDto.


        :param name: The name of this PublicTableDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def orientation(self):
        """Gets the orientation of this PublicTableDto.  # noqa: E501


        :return: The orientation of this PublicTableDto.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this PublicTableDto.


        :param orientation: The orientation of this PublicTableDto.  # noqa: E501
        :type: str
        """
        if orientation is None:
            raise ValueError("Invalid value for `orientation`, must not be `None`")  # noqa: E501
        allowed_values = ["HORIZONTAL", "VERTICAL"]  # noqa: E501
        if orientation not in allowed_values:
            raise ValueError(
                "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                .format(orientation, allowed_values)
            )

        self._orientation = orientation

    @property
    def values(self):
        """Gets the values of this PublicTableDto.  # noqa: E501


        :return: The values of this PublicTableDto.  # noqa: E501
        :rtype: list[Cells]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this PublicTableDto.


        :param values: The values of this PublicTableDto.  # noqa: E501
        :type: list[Cells]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PublicTableDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
