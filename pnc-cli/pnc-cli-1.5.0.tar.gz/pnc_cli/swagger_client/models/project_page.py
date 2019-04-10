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


class ProjectPage(object):
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
        'page_index': 'int',
        'page_size': 'int',
        'total_pages': 'int',
        'content': 'list[ProjectRest]'
    }

    attribute_map = {
        'page_index': 'pageIndex',
        'page_size': 'pageSize',
        'total_pages': 'totalPages',
        'content': 'content'
    }

    def __init__(self, page_index=None, page_size=None, total_pages=None, content=None):
        """
        ProjectPage - a model defined in Swagger
        """

        self._page_index = None
        self._page_size = None
        self._total_pages = None
        self._content = None

        if page_index is not None:
          self.page_index = page_index
        if page_size is not None:
          self.page_size = page_size
        if total_pages is not None:
          self.total_pages = total_pages
        if content is not None:
          self.content = content

    @property
    def page_index(self):
        """
        Gets the page_index of this ProjectPage.

        :return: The page_index of this ProjectPage.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this ProjectPage.

        :param page_index: The page_index of this ProjectPage.
        :type: int
        """

        self._page_index = page_index

    @property
    def page_size(self):
        """
        Gets the page_size of this ProjectPage.

        :return: The page_size of this ProjectPage.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this ProjectPage.

        :param page_size: The page_size of this ProjectPage.
        :type: int
        """

        self._page_size = page_size

    @property
    def total_pages(self):
        """
        Gets the total_pages of this ProjectPage.

        :return: The total_pages of this ProjectPage.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """
        Sets the total_pages of this ProjectPage.

        :param total_pages: The total_pages of this ProjectPage.
        :type: int
        """

        self._total_pages = total_pages

    @property
    def content(self):
        """
        Gets the content of this ProjectPage.

        :return: The content of this ProjectPage.
        :rtype: list[ProjectRest]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this ProjectPage.

        :param content: The content of this ProjectPage.
        :type: list[ProjectRest]
        """

        self._content = content

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
        if not isinstance(other, ProjectPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
