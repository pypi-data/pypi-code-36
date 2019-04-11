# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class CertificateDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CertificateDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'issuer': 'str',
            'subject': 'str',
            'expiration_date': 'datetime',
            'issue_date': 'datetime',
            'expired': 'bool',
            'signature_valid': 'bool',
            'valid': 'bool'
        }

        self.attribute_map = {
            'issuer': 'issuer',
            'subject': 'subject',
            'expiration_date': 'expirationDate',
            'issue_date': 'issueDate',
            'expired': 'expired',
            'signature_valid': 'signatureValid',
            'valid': 'valid'
        }

        self._issuer = None
        self._subject = None
        self._expiration_date = None
        self._issue_date = None
        self._expired = None
        self._signature_valid = None
        self._valid = None

    @property
    def issuer(self):
        """
        Gets the issuer of this CertificateDetails.
        Information about the issuer of the certificate.  The value of this property is a comma separated key=value format.  Each key is one of the attribute names supported by X.500.

        :return: The issuer of this CertificateDetails.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this CertificateDetails.
        Information about the issuer of the certificate.  The value of this property is a comma separated key=value format.  Each key is one of the attribute names supported by X.500.

        :param issuer: The issuer of this CertificateDetails.
        :type: str
        """
        
        self._issuer = issuer

    @property
    def subject(self):
        """
        Gets the subject of this CertificateDetails.
        Information about the subject of the certificate.  The value of this property is a comma separated key=value format.  Each key is one of the attribute names supported by X.500.

        :return: The subject of this CertificateDetails.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CertificateDetails.
        Information about the subject of the certificate.  The value of this property is a comma separated key=value format.  Each key is one of the attribute names supported by X.500.

        :param subject: The subject of this CertificateDetails.
        :type: str
        """
        
        self._subject = subject

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this CertificateDetails.
        The expiration date of the certificate. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The expiration_date of this CertificateDetails.
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this CertificateDetails.
        The expiration date of the certificate. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param expiration_date: The expiration_date of this CertificateDetails.
        :type: datetime
        """
        
        self._expiration_date = expiration_date

    @property
    def issue_date(self):
        """
        Gets the issue_date of this CertificateDetails.
        The issue date of the certificate. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The issue_date of this CertificateDetails.
        :rtype: datetime
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """
        Sets the issue_date of this CertificateDetails.
        The issue date of the certificate. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param issue_date: The issue_date of this CertificateDetails.
        :type: datetime
        """
        
        self._issue_date = issue_date

    @property
    def expired(self):
        """
        Gets the expired of this CertificateDetails.
        True if the certificate is expired, false otherwise.

        :return: The expired of this CertificateDetails.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """
        Sets the expired of this CertificateDetails.
        True if the certificate is expired, false otherwise.

        :param expired: The expired of this CertificateDetails.
        :type: bool
        """
        
        self._expired = expired

    @property
    def signature_valid(self):
        """
        Gets the signature_valid of this CertificateDetails.


        :return: The signature_valid of this CertificateDetails.
        :rtype: bool
        """
        return self._signature_valid

    @signature_valid.setter
    def signature_valid(self, signature_valid):
        """
        Sets the signature_valid of this CertificateDetails.


        :param signature_valid: The signature_valid of this CertificateDetails.
        :type: bool
        """
        
        self._signature_valid = signature_valid

    @property
    def valid(self):
        """
        Gets the valid of this CertificateDetails.


        :return: The valid of this CertificateDetails.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this CertificateDetails.


        :param valid: The valid of this CertificateDetails.
        :type: bool
        """
        
        self._valid = valid

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

