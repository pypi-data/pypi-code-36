# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class BuildConfigurationAuditedRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'rev': 'int',
        'id_rev': 'IdRev',
        'name': 'str',
        'description': 'str',
        'build_script': 'str',
        'repository_configuration': 'RepositoryConfigurationRest',
        'scm_revision': 'str',
        'creation_time': 'datetime',
        'last_modification_time': 'datetime',
        'project_id': 'int',
        'environment_id': 'int',
        'project': 'ProjectRest',
        'environment': 'BuildEnvironmentRest',
        'generic_parameters': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'rev': 'rev',
        'id_rev': 'idRev',
        'name': 'name',
        'description': 'description',
        'build_script': 'buildScript',
        'repository_configuration': 'repositoryConfiguration',
        'scm_revision': 'scmRevision',
        'creation_time': 'creationTime',
        'last_modification_time': 'lastModificationTime',
        'project_id': 'projectId',
        'environment_id': 'environmentId',
        'project': 'project',
        'environment': 'environment',
        'generic_parameters': 'genericParameters'
    }

    def __init__(self, id=None, rev=None, id_rev=None, name=None, description=None, build_script=None, repository_configuration=None, scm_revision=None, creation_time=None, last_modification_time=None, project_id=None, environment_id=None, project=None, environment=None, generic_parameters=None):
        """
        BuildConfigurationAuditedRest - a model defined in Swagger
        """

        self._id = None
        self._rev = None
        self._id_rev = None
        self._name = None
        self._description = None
        self._build_script = None
        self._repository_configuration = None
        self._scm_revision = None
        self._creation_time = None
        self._last_modification_time = None
        self._project_id = None
        self._environment_id = None
        self._project = None
        self._environment = None
        self._generic_parameters = None

        if id is not None:
          self.id = id
        if rev is not None:
          self.rev = rev
        if id_rev is not None:
          self.id_rev = id_rev
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if build_script is not None:
          self.build_script = build_script
        if repository_configuration is not None:
          self.repository_configuration = repository_configuration
        if scm_revision is not None:
          self.scm_revision = scm_revision
        if creation_time is not None:
          self.creation_time = creation_time
        if last_modification_time is not None:
          self.last_modification_time = last_modification_time
        if project_id is not None:
          self.project_id = project_id
        if environment_id is not None:
          self.environment_id = environment_id
        if project is not None:
          self.project = project
        if environment is not None:
          self.environment = environment
        if generic_parameters is not None:
          self.generic_parameters = generic_parameters

    @property
    def id(self):
        """
        Gets the id of this BuildConfigurationAuditedRest.

        :return: The id of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildConfigurationAuditedRest.

        :param id: The id of this BuildConfigurationAuditedRest.
        :type: int
        """

        self._id = id

    @property
    def rev(self):
        """
        Gets the rev of this BuildConfigurationAuditedRest.

        :return: The rev of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._rev

    @rev.setter
    def rev(self, rev):
        """
        Sets the rev of this BuildConfigurationAuditedRest.

        :param rev: The rev of this BuildConfigurationAuditedRest.
        :type: int
        """

        self._rev = rev

    @property
    def id_rev(self):
        """
        Gets the id_rev of this BuildConfigurationAuditedRest.

        :return: The id_rev of this BuildConfigurationAuditedRest.
        :rtype: IdRev
        """
        return self._id_rev

    @id_rev.setter
    def id_rev(self, id_rev):
        """
        Sets the id_rev of this BuildConfigurationAuditedRest.

        :param id_rev: The id_rev of this BuildConfigurationAuditedRest.
        :type: IdRev
        """

        self._id_rev = id_rev

    @property
    def name(self):
        """
        Gets the name of this BuildConfigurationAuditedRest.

        :return: The name of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildConfigurationAuditedRest.

        :param name: The name of this BuildConfigurationAuditedRest.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BuildConfigurationAuditedRest.

        :return: The description of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuildConfigurationAuditedRest.

        :param description: The description of this BuildConfigurationAuditedRest.
        :type: str
        """

        self._description = description

    @property
    def build_script(self):
        """
        Gets the build_script of this BuildConfigurationAuditedRest.

        :return: The build_script of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._build_script

    @build_script.setter
    def build_script(self, build_script):
        """
        Sets the build_script of this BuildConfigurationAuditedRest.

        :param build_script: The build_script of this BuildConfigurationAuditedRest.
        :type: str
        """

        self._build_script = build_script

    @property
    def repository_configuration(self):
        """
        Gets the repository_configuration of this BuildConfigurationAuditedRest.

        :return: The repository_configuration of this BuildConfigurationAuditedRest.
        :rtype: RepositoryConfigurationRest
        """
        return self._repository_configuration

    @repository_configuration.setter
    def repository_configuration(self, repository_configuration):
        """
        Sets the repository_configuration of this BuildConfigurationAuditedRest.

        :param repository_configuration: The repository_configuration of this BuildConfigurationAuditedRest.
        :type: RepositoryConfigurationRest
        """

        self._repository_configuration = repository_configuration

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BuildConfigurationAuditedRest.

        :return: The scm_revision of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BuildConfigurationAuditedRest.

        :param scm_revision: The scm_revision of this BuildConfigurationAuditedRest.
        :type: str
        """

        self._scm_revision = scm_revision

    @property
    def creation_time(self):
        """
        Gets the creation_time of this BuildConfigurationAuditedRest.

        :return: The creation_time of this BuildConfigurationAuditedRest.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this BuildConfigurationAuditedRest.

        :param creation_time: The creation_time of this BuildConfigurationAuditedRest.
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def last_modification_time(self):
        """
        Gets the last_modification_time of this BuildConfigurationAuditedRest.

        :return: The last_modification_time of this BuildConfigurationAuditedRest.
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """
        Sets the last_modification_time of this BuildConfigurationAuditedRest.

        :param last_modification_time: The last_modification_time of this BuildConfigurationAuditedRest.
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def project_id(self):
        """
        Gets the project_id of this BuildConfigurationAuditedRest.

        :return: The project_id of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this BuildConfigurationAuditedRest.

        :param project_id: The project_id of this BuildConfigurationAuditedRest.
        :type: int
        """

        self._project_id = project_id

    @property
    def environment_id(self):
        """
        Gets the environment_id of this BuildConfigurationAuditedRest.

        :return: The environment_id of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this BuildConfigurationAuditedRest.

        :param environment_id: The environment_id of this BuildConfigurationAuditedRest.
        :type: int
        """

        self._environment_id = environment_id

    @property
    def project(self):
        """
        Gets the project of this BuildConfigurationAuditedRest.

        :return: The project of this BuildConfigurationAuditedRest.
        :rtype: ProjectRest
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this BuildConfigurationAuditedRest.

        :param project: The project of this BuildConfigurationAuditedRest.
        :type: ProjectRest
        """

        self._project = project

    @property
    def environment(self):
        """
        Gets the environment of this BuildConfigurationAuditedRest.

        :return: The environment of this BuildConfigurationAuditedRest.
        :rtype: BuildEnvironmentRest
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this BuildConfigurationAuditedRest.

        :param environment: The environment of this BuildConfigurationAuditedRest.
        :type: BuildEnvironmentRest
        """

        self._environment = environment

    @property
    def generic_parameters(self):
        """
        Gets the generic_parameters of this BuildConfigurationAuditedRest.

        :return: The generic_parameters of this BuildConfigurationAuditedRest.
        :rtype: dict(str, str)
        """
        return self._generic_parameters

    @generic_parameters.setter
    def generic_parameters(self, generic_parameters):
        """
        Sets the generic_parameters of this BuildConfigurationAuditedRest.

        :param generic_parameters: The generic_parameters of this BuildConfigurationAuditedRest.
        :type: dict(str, str)
        """

        self._generic_parameters = generic_parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
            elif isinstance(value, datetime):
                result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BuildConfigurationAuditedRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
