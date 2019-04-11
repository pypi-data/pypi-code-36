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


class Payments(object):
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
        'invoice': 'str'
    }

    attribute_map = {
        'invoice': 'invoice'
    }

    def __init__(self, invoice=None):  # noqa: E501
        """Payments - a model defined in OpenAPI"""  # noqa: E501

        self._invoice = None
        self.discriminator = None

        if invoice is not None:
            self.invoice = invoice

    @property
    def invoice(self):
        """Gets the invoice of this Payments.  # noqa: E501

        Invoice type, one of: VAT, VAT_MARGIN, WITHOUT_VAT, NO_INVOICE  # noqa: E501

        :return: The invoice of this Payments.  # noqa: E501
        :rtype: str
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this Payments.

        Invoice type, one of: VAT, VAT_MARGIN, WITHOUT_VAT, NO_INVOICE  # noqa: E501

        :param invoice: The invoice of this Payments.  # noqa: E501
        :type: str
        """

        self._invoice = invoice

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
        if not isinstance(other, Payments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
