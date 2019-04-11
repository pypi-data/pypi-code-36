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


class WrapperTypeForPreviewConditions(object):
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
        'include_quoting_bundles': 'bool',
        'offer': 'ParametersForPreviewPrice'
    }

    attribute_map = {
        'include_quoting_bundles': 'includeQuotingBundles',
        'offer': 'offer'
    }

    def __init__(self, include_quoting_bundles=None, offer=None):  # noqa: E501
        """WrapperTypeForPreviewConditions - a model defined in OpenAPI"""  # noqa: E501

        self._include_quoting_bundles = None
        self._offer = None
        self.discriminator = None

        if include_quoting_bundles is not None:
            self.include_quoting_bundles = include_quoting_bundles
        if offer is not None:
            self.offer = offer

    @property
    def include_quoting_bundles(self):
        """Gets the include_quoting_bundles of this WrapperTypeForPreviewConditions.  # noqa: E501

        Include in calculation user's active bundles which allow to publish for free offer or use for free promotion options.  # noqa: E501

        :return: The include_quoting_bundles of this WrapperTypeForPreviewConditions.  # noqa: E501
        :rtype: bool
        """
        return self._include_quoting_bundles

    @include_quoting_bundles.setter
    def include_quoting_bundles(self, include_quoting_bundles):
        """Sets the include_quoting_bundles of this WrapperTypeForPreviewConditions.

        Include in calculation user's active bundles which allow to publish for free offer or use for free promotion options.  # noqa: E501

        :param include_quoting_bundles: The include_quoting_bundles of this WrapperTypeForPreviewConditions.  # noqa: E501
        :type: bool
        """

        self._include_quoting_bundles = include_quoting_bundles

    @property
    def offer(self):
        """Gets the offer of this WrapperTypeForPreviewConditions.  # noqa: E501


        :return: The offer of this WrapperTypeForPreviewConditions.  # noqa: E501
        :rtype: ParametersForPreviewPrice
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this WrapperTypeForPreviewConditions.


        :param offer: The offer of this WrapperTypeForPreviewConditions.  # noqa: E501
        :type: ParametersForPreviewPrice
        """

        self._offer = offer

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
        if not isinstance(other, WrapperTypeForPreviewConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
