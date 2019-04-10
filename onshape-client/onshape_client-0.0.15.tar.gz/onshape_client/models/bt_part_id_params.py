# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.96
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTPartIdParams(object):
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
        'ids': 'list[str]',
        'link_document_id': 'str',
        'configuration': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'link_document_id': 'linkDocumentId',
        'configuration': 'configuration'
    }

    def __init__(self, ids=None, link_document_id=None, configuration=None):  # noqa: E501
        """BTPartIdParams - a model defined in OpenAPI"""  # noqa: E501

        self._ids = None
        self._link_document_id = None
        self._configuration = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if link_document_id is not None:
            self.link_document_id = link_document_id
        if configuration is not None:
            self.configuration = configuration

    @property
    def ids(self):
        """Gets the ids of this BTPartIdParams.  # noqa: E501


        :return: The ids of this BTPartIdParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this BTPartIdParams.


        :param ids: The ids of this BTPartIdParams.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def link_document_id(self):
        """Gets the link_document_id of this BTPartIdParams.  # noqa: E501


        :return: The link_document_id of this BTPartIdParams.  # noqa: E501
        :rtype: str
        """
        return self._link_document_id

    @link_document_id.setter
    def link_document_id(self, link_document_id):
        """Sets the link_document_id of this BTPartIdParams.


        :param link_document_id: The link_document_id of this BTPartIdParams.  # noqa: E501
        :type: str
        """

        self._link_document_id = link_document_id

    @property
    def configuration(self):
        """Gets the configuration of this BTPartIdParams.  # noqa: E501


        :return: The configuration of this BTPartIdParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTPartIdParams.


        :param configuration: The configuration of this BTPartIdParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

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
        if not isinstance(other, BTPartIdParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
