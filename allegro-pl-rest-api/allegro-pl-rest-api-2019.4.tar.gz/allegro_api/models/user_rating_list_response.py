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


class UserRatingListResponse(object):
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
        'ratings': 'list[UserRating]'
    }

    attribute_map = {
        'ratings': 'ratings'
    }

    def __init__(self, ratings=None):  # noqa: E501
        """UserRatingListResponse - a model defined in OpenAPI"""  # noqa: E501

        self._ratings = None
        self.discriminator = None

        self.ratings = ratings

    @property
    def ratings(self):
        """Gets the ratings of this UserRatingListResponse.  # noqa: E501

        List of ratings that match requested filter. Empty when no rating matched.  # noqa: E501

        :return: The ratings of this UserRatingListResponse.  # noqa: E501
        :rtype: list[UserRating]
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this UserRatingListResponse.

        List of ratings that match requested filter. Empty when no rating matched.  # noqa: E501

        :param ratings: The ratings of this UserRatingListResponse.  # noqa: E501
        :type: list[UserRating]
        """
        if ratings is None:
            raise ValueError("Invalid value for `ratings`, must not be `None`")  # noqa: E501

        self._ratings = ratings

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
        if not isinstance(other, UserRatingListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
