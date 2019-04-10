# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class CompanyNews(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'title': 'str',
        'publication_date': 'datetime',
        'url': 'str',
        'summary': 'str',
        'company': 'CompanySummary'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'publication_date': 'publication_date',
        'url': 'url',
        'summary': 'summary',
        'company': 'company'
    }

    def __init__(self, id=None, title=None, publication_date=None, url=None, summary=None, company=None):  # noqa: E501
        """CompanyNews - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._publication_date = None
        self._url = None
        self._summary = None
        self._company = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if publication_date is not None:
            self.publication_date = publication_date
        if url is not None:
            self.url = url
        if summary is not None:
            self.summary = summary
        if company is not None:
            self.company = company

    @property
    def id(self):
        """Gets the id of this CompanyNews.  # noqa: E501

        The Intrinio ID for the news article  # noqa: E501

        :return: The id of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this CompanyNews.  # noqa: E501

        The Intrinio ID for the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = getattr(self, id)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyNews.

        The Intrinio ID for the news article  # noqa: E501

        :param id: The id of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this CompanyNews.  # noqa: E501

        The title of the news article  # noqa: E501

        :return: The title of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._title
        
    @property
    def title_dict(self):
        """Gets the title of this CompanyNews.  # noqa: E501

        The title of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The title of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = getattr(self, title)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'title': value }

        
        return result
        

    @title.setter
    def title(self, title):
        """Sets the title of this CompanyNews.

        The title of the news article  # noqa: E501

        :param title: The title of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def publication_date(self):
        """Gets the publication_date of this CompanyNews.  # noqa: E501

        The publication date of the news article  # noqa: E501

        :return: The publication_date of this CompanyNews.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date
        
    @property
    def publication_date_dict(self):
        """Gets the publication_date of this CompanyNews.  # noqa: E501

        The publication date of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The publication_date of this CompanyNews.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = getattr(self, publication_date)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'publication_date': value }

        
        return result
        

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this CompanyNews.

        The publication date of the news article  # noqa: E501

        :param publication_date: The publication_date of this CompanyNews.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def url(self):
        """Gets the url of this CompanyNews.  # noqa: E501

        The url of the news article  # noqa: E501

        :return: The url of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._url
        
    @property
    def url_dict(self):
        """Gets the url of this CompanyNews.  # noqa: E501

        The url of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The url of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = getattr(self, url)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'url': value }

        
        return result
        

    @url.setter
    def url(self, url):
        """Sets the url of this CompanyNews.

        The url of the news article  # noqa: E501

        :param url: The url of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def summary(self):
        """Gets the summary of this CompanyNews.  # noqa: E501

        A summary of the news article  # noqa: E501

        :return: The summary of this CompanyNews.  # noqa: E501
        :rtype: str
        """
        return self._summary
        
    @property
    def summary_dict(self):
        """Gets the summary of this CompanyNews.  # noqa: E501

        A summary of the news article as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The summary of this CompanyNews.  # noqa: E501
        :rtype: str
        """

        result = None

        value = getattr(self, summary)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'summary': value }

        
        return result
        

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this CompanyNews.

        A summary of the news article  # noqa: E501

        :param summary: The summary of this CompanyNews.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def company(self):
        """Gets the company of this CompanyNews.  # noqa: E501

        The Company that the Fundamental was belongs to  # noqa: E501

        :return: The company of this CompanyNews.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this CompanyNews.  # noqa: E501

        The Company that the Fundamental was belongs to as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company of this CompanyNews.  # noqa: E501
        :rtype: CompanySummary
        """

        result = None

        value = getattr(self, company)
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'company': value }

        
        return result
        

    @company.setter
    def company(self, company):
        """Sets the company of this CompanyNews.

        The Company that the Fundamental was belongs to  # noqa: E501

        :param company: The company of this CompanyNews.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

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
        if not isinstance(other, CompanyNews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
