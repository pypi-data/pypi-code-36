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


class VariantSets(object):
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
        'count': 'int',
        'offer_variants': 'list[VariantSetsVariantSet]'
    }

    attribute_map = {
        'count': 'count',
        'offer_variants': 'offerVariants'
    }

    def __init__(self, count=None, offer_variants=None):  # noqa: E501
        """VariantSets - a model defined in OpenAPI"""  # noqa: E501

        self._count = None
        self._offer_variants = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if offer_variants is not None:
            self.offer_variants = offer_variants

    @property
    def count(self):
        """Gets the count of this VariantSets.  # noqa: E501

        Total number of variant sets matching the query.  # noqa: E501

        :return: The count of this VariantSets.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VariantSets.

        Total number of variant sets matching the query.  # noqa: E501

        :param count: The count of this VariantSets.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def offer_variants(self):
        """Gets the offer_variants of this VariantSets.  # noqa: E501


        :return: The offer_variants of this VariantSets.  # noqa: E501
        :rtype: list[VariantSetsVariantSet]
        """
        return self._offer_variants

    @offer_variants.setter
    def offer_variants(self, offer_variants):
        """Sets the offer_variants of this VariantSets.


        :param offer_variants: The offer_variants of this VariantSets.  # noqa: E501
        :type: list[VariantSetsVariantSet]
        """

        self._offer_variants = offer_variants

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
        if not isinstance(other, VariantSets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
