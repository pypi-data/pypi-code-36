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


class OfferListingDtoV1Stats(object):
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
        'watchers_count': 'int',
        'visits_count': 'int'
    }

    attribute_map = {
        'watchers_count': 'watchersCount',
        'visits_count': 'visitsCount'
    }

    def __init__(self, watchers_count=None, visits_count=None):  # noqa: E501
        """OfferListingDtoV1Stats - a model defined in OpenAPI"""  # noqa: E501

        self._watchers_count = None
        self._visits_count = None
        self.discriminator = None

        if watchers_count is not None:
            self.watchers_count = watchers_count
        if visits_count is not None:
            self.visits_count = visits_count

    @property
    def watchers_count(self):
        """Gets the watchers_count of this OfferListingDtoV1Stats.  # noqa: E501

        Number of users that added this offer to watching offers list  # noqa: E501

        :return: The watchers_count of this OfferListingDtoV1Stats.  # noqa: E501
        :rtype: int
        """
        return self._watchers_count

    @watchers_count.setter
    def watchers_count(self, watchers_count):
        """Sets the watchers_count of this OfferListingDtoV1Stats.

        Number of users that added this offer to watching offers list  # noqa: E501

        :param watchers_count: The watchers_count of this OfferListingDtoV1Stats.  # noqa: E501
        :type: int
        """

        self._watchers_count = watchers_count

    @property
    def visits_count(self):
        """Gets the visits_count of this OfferListingDtoV1Stats.  # noqa: E501

        Number of users visits from past 30 days. Any number of offer shows during the same day by the same user is one visit.  # noqa: E501

        :return: The visits_count of this OfferListingDtoV1Stats.  # noqa: E501
        :rtype: int
        """
        return self._visits_count

    @visits_count.setter
    def visits_count(self, visits_count):
        """Sets the visits_count of this OfferListingDtoV1Stats.

        Number of users visits from past 30 days. Any number of offer shows during the same day by the same user is one visit.  # noqa: E501

        :param visits_count: The visits_count of this OfferListingDtoV1Stats.  # noqa: E501
        :type: int
        """

        self._visits_count = visits_count

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
        if not isinstance(other, OfferListingDtoV1Stats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
