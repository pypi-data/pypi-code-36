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


class PublicationChangeCommandDto(object):
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
        'offer_criteria': 'list[OfferCriterium]',
        'publication': 'PublicationModification'
    }

    attribute_map = {
        'offer_criteria': 'offerCriteria',
        'publication': 'publication'
    }

    def __init__(self, offer_criteria=None, publication=None):  # noqa: E501
        """PublicationChangeCommandDto - a model defined in OpenAPI"""  # noqa: E501

        self._offer_criteria = None
        self._publication = None
        self.discriminator = None

        if offer_criteria is not None:
            self.offer_criteria = offer_criteria
        if publication is not None:
            self.publication = publication

    @property
    def offer_criteria(self):
        """Gets the offer_criteria of this PublicationChangeCommandDto.  # noqa: E501

        List of offer criteria  # noqa: E501

        :return: The offer_criteria of this PublicationChangeCommandDto.  # noqa: E501
        :rtype: list[OfferCriterium]
        """
        return self._offer_criteria

    @offer_criteria.setter
    def offer_criteria(self, offer_criteria):
        """Sets the offer_criteria of this PublicationChangeCommandDto.

        List of offer criteria  # noqa: E501

        :param offer_criteria: The offer_criteria of this PublicationChangeCommandDto.  # noqa: E501
        :type: list[OfferCriterium]
        """

        self._offer_criteria = offer_criteria

    @property
    def publication(self):
        """Gets the publication of this PublicationChangeCommandDto.  # noqa: E501


        :return: The publication of this PublicationChangeCommandDto.  # noqa: E501
        :rtype: PublicationModification
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this PublicationChangeCommandDto.


        :param publication: The publication of this PublicationChangeCommandDto.  # noqa: E501
        :type: PublicationModification
        """

        self._publication = publication

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
        if not isinstance(other, PublicationChangeCommandDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
