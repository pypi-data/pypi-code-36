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


class ProductReleaseRest(object):
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
        'version': 'str',
        'release_date': 'datetime',
        'download_url': 'str',
        'issue_tracker_url': 'str',
        'product_version_id': 'int',
        'product_milestone_id': 'int',
        'support_level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'release_date': 'releaseDate',
        'download_url': 'downloadUrl',
        'issue_tracker_url': 'issueTrackerUrl',
        'product_version_id': 'productVersionId',
        'product_milestone_id': 'productMilestoneId',
        'support_level': 'supportLevel'
    }

    def __init__(self, id=None, version=None, release_date=None, download_url=None, issue_tracker_url=None, product_version_id=None, product_milestone_id=None, support_level=None):
        """
        ProductReleaseRest - a model defined in Swagger
        """

        self._id = None
        self._version = None
        self._release_date = None
        self._download_url = None
        self._issue_tracker_url = None
        self._product_version_id = None
        self._product_milestone_id = None
        self._support_level = None

        if id is not None:
          self.id = id
        if version is not None:
          self.version = version
        if release_date is not None:
          self.release_date = release_date
        if download_url is not None:
          self.download_url = download_url
        if issue_tracker_url is not None:
          self.issue_tracker_url = issue_tracker_url
        if product_version_id is not None:
          self.product_version_id = product_version_id
        if product_milestone_id is not None:
          self.product_milestone_id = product_milestone_id
        if support_level is not None:
          self.support_level = support_level

    @property
    def id(self):
        """
        Gets the id of this ProductReleaseRest.

        :return: The id of this ProductReleaseRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductReleaseRest.

        :param id: The id of this ProductReleaseRest.
        :type: int
        """

        self._id = id

    @property
    def version(self):
        """
        Gets the version of this ProductReleaseRest.

        :return: The version of this ProductReleaseRest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductReleaseRest.

        :param version: The version of this ProductReleaseRest.
        :type: str
        """

        self._version = version

    @property
    def release_date(self):
        """
        Gets the release_date of this ProductReleaseRest.

        :return: The release_date of this ProductReleaseRest.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this ProductReleaseRest.

        :param release_date: The release_date of this ProductReleaseRest.
        :type: datetime
        """

        self._release_date = release_date

    @property
    def download_url(self):
        """
        Gets the download_url of this ProductReleaseRest.

        :return: The download_url of this ProductReleaseRest.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ProductReleaseRest.

        :param download_url: The download_url of this ProductReleaseRest.
        :type: str
        """

        self._download_url = download_url

    @property
    def issue_tracker_url(self):
        """
        Gets the issue_tracker_url of this ProductReleaseRest.

        :return: The issue_tracker_url of this ProductReleaseRest.
        :rtype: str
        """
        return self._issue_tracker_url

    @issue_tracker_url.setter
    def issue_tracker_url(self, issue_tracker_url):
        """
        Sets the issue_tracker_url of this ProductReleaseRest.

        :param issue_tracker_url: The issue_tracker_url of this ProductReleaseRest.
        :type: str
        """

        self._issue_tracker_url = issue_tracker_url

    @property
    def product_version_id(self):
        """
        Gets the product_version_id of this ProductReleaseRest.

        :return: The product_version_id of this ProductReleaseRest.
        :rtype: int
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """
        Sets the product_version_id of this ProductReleaseRest.

        :param product_version_id: The product_version_id of this ProductReleaseRest.
        :type: int
        """

        self._product_version_id = product_version_id

    @property
    def product_milestone_id(self):
        """
        Gets the product_milestone_id of this ProductReleaseRest.

        :return: The product_milestone_id of this ProductReleaseRest.
        :rtype: int
        """
        return self._product_milestone_id

    @product_milestone_id.setter
    def product_milestone_id(self, product_milestone_id):
        """
        Sets the product_milestone_id of this ProductReleaseRest.

        :param product_milestone_id: The product_milestone_id of this ProductReleaseRest.
        :type: int
        """

        self._product_milestone_id = product_milestone_id

    @property
    def support_level(self):
        """
        Gets the support_level of this ProductReleaseRest.

        :return: The support_level of this ProductReleaseRest.
        :rtype: str
        """
        return self._support_level

    @support_level.setter
    def support_level(self, support_level):
        """
        Sets the support_level of this ProductReleaseRest.

        :param support_level: The support_level of this ProductReleaseRest.
        :type: str
        """
        allowed_values = ["UNRELEASED", "EARLYACCESS", "SUPPORTED", "EXTENDED_SUPPORT", "EOL"]
        if support_level not in allowed_values:
            raise ValueError(
                "Invalid value for `support_level` ({0}), must be one of {1}"
                .format(support_level, allowed_values)
            )

        self._support_level = support_level

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
        if not isinstance(other, ProductReleaseRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
