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


class OffersSearchResultDtoV1(object):
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
        'offers': 'list[OfferListingDtoV1]',
        'count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'offers': 'offers',
        'count': 'count',
        'total_count': 'totalCount'
    }

    def __init__(self, offers=None, count=None, total_count=None):  # noqa: E501
        """OffersSearchResultDtoV1 - a model defined in OpenAPI"""  # noqa: E501

        self._offers = None
        self._count = None
        self._total_count = None
        self.discriminator = None

        if offers is not None:
            self.offers = offers
        if count is not None:
            self.count = count
        if total_count is not None:
            self.total_count = total_count

    @property
    def offers(self):
        """Gets the offers of this OffersSearchResultDtoV1.  # noqa: E501


        :return: The offers of this OffersSearchResultDtoV1.  # noqa: E501
        :rtype: list[OfferListingDtoV1]
        """
        return self._offers

    @offers.setter
    def offers(self, offers):
        """Sets the offers of this OffersSearchResultDtoV1.


        :param offers: The offers of this OffersSearchResultDtoV1.  # noqa: E501
        :type: list[OfferListingDtoV1]
        """

        self._offers = offers

    @property
    def count(self):
        """Gets the count of this OffersSearchResultDtoV1.  # noqa: E501

        Number of offers in search result for given parameters  # noqa: E501

        :return: The count of this OffersSearchResultDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this OffersSearchResultDtoV1.

        Number of offers in search result for given parameters  # noqa: E501

        :param count: The count of this OffersSearchResultDtoV1.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def total_count(self):
        """Gets the total_count of this OffersSearchResultDtoV1.  # noqa: E501

        Total number of offers for given parameters  # noqa: E501

        :return: The total_count of this OffersSearchResultDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this OffersSearchResultDtoV1.

        Total number of offers for given parameters  # noqa: E501

        :param total_count: The total_count of this OffersSearchResultDtoV1.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, OffersSearchResultDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
