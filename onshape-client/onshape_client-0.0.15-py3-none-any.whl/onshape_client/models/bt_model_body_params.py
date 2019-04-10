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


class BTModelBodyParams(object):
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
        'configuration': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'part_query': 'str',
        'part_id': 'str',
        'document_id': 'str',
        'element_microversion_id': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'part_query': 'partQuery',
        'part_id': 'partId',
        'document_id': 'documentId',
        'element_microversion_id': 'elementMicroversionId'
    }

    def __init__(self, configuration=None, workspace_id=None, element_id=None, part_query=None, part_id=None, document_id=None, element_microversion_id=None):  # noqa: E501
        """BTModelBodyParams - a model defined in OpenAPI"""  # noqa: E501

        self._configuration = None
        self._workspace_id = None
        self._element_id = None
        self._part_query = None
        self._part_id = None
        self._document_id = None
        self._element_microversion_id = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if part_query is not None:
            self.part_query = part_query
        if part_id is not None:
            self.part_id = part_id
        if document_id is not None:
            self.document_id = document_id
        if element_microversion_id is not None:
            self.element_microversion_id = element_microversion_id

    @property
    def configuration(self):
        """Gets the configuration of this BTModelBodyParams.  # noqa: E501


        :return: The configuration of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTModelBodyParams.


        :param configuration: The configuration of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTModelBodyParams.  # noqa: E501


        :return: The workspace_id of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTModelBodyParams.


        :param workspace_id: The workspace_id of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTModelBodyParams.  # noqa: E501


        :return: The element_id of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTModelBodyParams.


        :param element_id: The element_id of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def part_query(self):
        """Gets the part_query of this BTModelBodyParams.  # noqa: E501


        :return: The part_query of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._part_query

    @part_query.setter
    def part_query(self, part_query):
        """Sets the part_query of this BTModelBodyParams.


        :param part_query: The part_query of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._part_query = part_query

    @property
    def part_id(self):
        """Gets the part_id of this BTModelBodyParams.  # noqa: E501


        :return: The part_id of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTModelBodyParams.


        :param part_id: The part_id of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def document_id(self):
        """Gets the document_id of this BTModelBodyParams.  # noqa: E501


        :return: The document_id of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTModelBodyParams.


        :param document_id: The document_id of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def element_microversion_id(self):
        """Gets the element_microversion_id of this BTModelBodyParams.  # noqa: E501


        :return: The element_microversion_id of this BTModelBodyParams.  # noqa: E501
        :rtype: str
        """
        return self._element_microversion_id

    @element_microversion_id.setter
    def element_microversion_id(self, element_microversion_id):
        """Sets the element_microversion_id of this BTModelBodyParams.


        :param element_microversion_id: The element_microversion_id of this BTModelBodyParams.  # noqa: E501
        :type: str
        """

        self._element_microversion_id = element_microversion_id

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
        if not isinstance(other, BTModelBodyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
