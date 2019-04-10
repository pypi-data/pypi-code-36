# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1.0-dev.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.permission import Permission  # noqa: F401,E501
from flywheel.models.search_acquisition_response import SearchAcquisitionResponse  # noqa: F401,E501
from flywheel.models.search_analysis_response import SearchAnalysisResponse  # noqa: F401,E501
from flywheel.models.search_collection_response import SearchCollectionResponse  # noqa: F401,E501
from flywheel.models.search_file_response import SearchFileResponse  # noqa: F401,E501
from flywheel.models.search_group_response import SearchGroupResponse  # noqa: F401,E501
from flywheel.models.search_parent_response import SearchParentResponse  # noqa: F401,E501
from flywheel.models.search_project_response import SearchProjectResponse  # noqa: F401,E501
from flywheel.models.search_session_response import SearchSessionResponse  # noqa: F401,E501
from flywheel.models.search_subject_response import SearchSubjectResponse  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

from .mixins import SearchResponseMixin

class SearchResponse(SearchResponseMixin):

    swagger_types = {
        'return_type': 'str',
        'project': 'SearchProjectResponse',
        'group': 'SearchGroupResponse',
        'session': 'SearchSessionResponse',
        'acquisition': 'SearchAcquisitionResponse',
        'subject': 'SearchSubjectResponse',
        'file': 'SearchFileResponse',
        'collection': 'SearchCollectionResponse',
        'analysis': 'SearchAnalysisResponse',
        'parent': 'SearchParentResponse',
        'permissions': 'list[Permission]'
    }

    attribute_map = {
        'return_type': 'return_type',
        'project': 'project',
        'group': 'group',
        'session': 'session',
        'acquisition': 'acquisition',
        'subject': 'subject',
        'file': 'file',
        'collection': 'collection',
        'analysis': 'analysis',
        'parent': 'parent',
        'permissions': 'permissions'
    }

    rattribute_map = {
        'return_type': 'return_type',
        'project': 'project',
        'group': 'group',
        'session': 'session',
        'acquisition': 'acquisition',
        'subject': 'subject',
        'file': 'file',
        'collection': 'collection',
        'analysis': 'analysis',
        'parent': 'parent',
        'permissions': 'permissions'
    }

    def __init__(self, return_type=None, project=None, group=None, session=None, acquisition=None, subject=None, file=None, collection=None, analysis=None, parent=None, permissions=None):  # noqa: E501
        """SearchResponse - a model defined in Swagger"""
        super(SearchResponse, self).__init__()

        self._return_type = None
        self._project = None
        self._group = None
        self._session = None
        self._acquisition = None
        self._subject = None
        self._file = None
        self._collection = None
        self._analysis = None
        self._parent = None
        self._permissions = None
        self.discriminator = None
        self.alt_discriminator = None

        if return_type is not None:
            self.return_type = return_type
        if project is not None:
            self.project = project
        if group is not None:
            self.group = group
        if session is not None:
            self.session = session
        if acquisition is not None:
            self.acquisition = acquisition
        if subject is not None:
            self.subject = subject
        if file is not None:
            self.file = file
        if collection is not None:
            self.collection = collection
        if analysis is not None:
            self.analysis = analysis
        if parent is not None:
            self.parent = parent
        if permissions is not None:
            self.permissions = permissions

    @property
    def return_type(self):
        """Gets the return_type of this SearchResponse.

        Sets the type of search results to return

        :return: The return_type of this SearchResponse.
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets the return_type of this SearchResponse.

        Sets the type of search results to return

        :param return_type: The return_type of this SearchResponse.  # noqa: E501
        :type: str
        """

        self._return_type = return_type

    @property
    def project(self):
        """Gets the project of this SearchResponse.


        :return: The project of this SearchResponse.
        :rtype: SearchProjectResponse
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this SearchResponse.


        :param project: The project of this SearchResponse.  # noqa: E501
        :type: SearchProjectResponse
        """

        self._project = project

    @property
    def group(self):
        """Gets the group of this SearchResponse.


        :return: The group of this SearchResponse.
        :rtype: SearchGroupResponse
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SearchResponse.


        :param group: The group of this SearchResponse.  # noqa: E501
        :type: SearchGroupResponse
        """

        self._group = group

    @property
    def session(self):
        """Gets the session of this SearchResponse.


        :return: The session of this SearchResponse.
        :rtype: SearchSessionResponse
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this SearchResponse.


        :param session: The session of this SearchResponse.  # noqa: E501
        :type: SearchSessionResponse
        """

        self._session = session

    @property
    def acquisition(self):
        """Gets the acquisition of this SearchResponse.


        :return: The acquisition of this SearchResponse.
        :rtype: SearchAcquisitionResponse
        """
        return self._acquisition

    @acquisition.setter
    def acquisition(self, acquisition):
        """Sets the acquisition of this SearchResponse.


        :param acquisition: The acquisition of this SearchResponse.  # noqa: E501
        :type: SearchAcquisitionResponse
        """

        self._acquisition = acquisition

    @property
    def subject(self):
        """Gets the subject of this SearchResponse.


        :return: The subject of this SearchResponse.
        :rtype: SearchSubjectResponse
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SearchResponse.


        :param subject: The subject of this SearchResponse.  # noqa: E501
        :type: SearchSubjectResponse
        """

        self._subject = subject

    @property
    def file(self):
        """Gets the file of this SearchResponse.


        :return: The file of this SearchResponse.
        :rtype: SearchFileResponse
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SearchResponse.


        :param file: The file of this SearchResponse.  # noqa: E501
        :type: SearchFileResponse
        """

        self._file = file

    @property
    def collection(self):
        """Gets the collection of this SearchResponse.


        :return: The collection of this SearchResponse.
        :rtype: SearchCollectionResponse
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this SearchResponse.


        :param collection: The collection of this SearchResponse.  # noqa: E501
        :type: SearchCollectionResponse
        """

        self._collection = collection

    @property
    def analysis(self):
        """Gets the analysis of this SearchResponse.


        :return: The analysis of this SearchResponse.
        :rtype: SearchAnalysisResponse
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this SearchResponse.


        :param analysis: The analysis of this SearchResponse.  # noqa: E501
        :type: SearchAnalysisResponse
        """

        self._analysis = analysis

    @property
    def parent(self):
        """Gets the parent of this SearchResponse.


        :return: The parent of this SearchResponse.
        :rtype: SearchParentResponse
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this SearchResponse.


        :param parent: The parent of this SearchResponse.  # noqa: E501
        :type: SearchParentResponse
        """

        self._parent = parent

    @property
    def permissions(self):
        """Gets the permissions of this SearchResponse.

        Array of user roles

        :return: The permissions of this SearchResponse.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this SearchResponse.

        Array of user roles

        :param permissions: The permissions of this SearchResponse.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, SearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
