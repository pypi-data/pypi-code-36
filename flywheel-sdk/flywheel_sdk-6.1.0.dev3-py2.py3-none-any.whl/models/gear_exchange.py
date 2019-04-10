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

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class GearExchange(object):

    swagger_types = {
        'git_commit': 'str',
        'rootfs_hash': 'str',
        'rootfs_url': 'str'
    }

    attribute_map = {
        'git_commit': 'git-commit',
        'rootfs_hash': 'rootfs-hash',
        'rootfs_url': 'rootfs-url'
    }

    rattribute_map = {
        'git-commit': 'git_commit',
        'rootfs-hash': 'rootfs_hash',
        'rootfs-url': 'rootfs_url'
    }

    def __init__(self, git_commit=None, rootfs_hash=None, rootfs_url=None):  # noqa: E501
        """GearExchange - a model defined in Swagger"""
        super(GearExchange, self).__init__()

        self._git_commit = None
        self._rootfs_hash = None
        self._rootfs_url = None
        self.discriminator = None
        self.alt_discriminator = None

        self.git_commit = git_commit
        self.rootfs_hash = rootfs_hash
        self.rootfs_url = rootfs_url

    @property
    def git_commit(self):
        """Gets the git_commit of this GearExchange.

        The SHA-1 hash referring to the git commit

        :return: The git_commit of this GearExchange.
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this GearExchange.

        The SHA-1 hash referring to the git commit

        :param git_commit: The git_commit of this GearExchange.  # noqa: E501
        :type: str
        """

        self._git_commit = git_commit

    @property
    def rootfs_hash(self):
        """Gets the rootfs_hash of this GearExchange.

        The cryptographic hash of the root filesystem in the form of \"algorithm:<base16 hash>\"

        :return: The rootfs_hash of this GearExchange.
        :rtype: str
        """
        return self._rootfs_hash

    @rootfs_hash.setter
    def rootfs_hash(self, rootfs_hash):
        """Sets the rootfs_hash of this GearExchange.

        The cryptographic hash of the root filesystem in the form of \"algorithm:<base16 hash>\"

        :param rootfs_hash: The rootfs_hash of this GearExchange.  # noqa: E501
        :type: str
        """

        self._rootfs_hash = rootfs_hash

    @property
    def rootfs_url(self):
        """Gets the rootfs_url of this GearExchange.

        The absolute URL of the gear's root file system

        :return: The rootfs_url of this GearExchange.
        :rtype: str
        """
        return self._rootfs_url

    @rootfs_url.setter
    def rootfs_url(self, rootfs_url):
        """Sets the rootfs_url of this GearExchange.

        The absolute URL of the gear's root file system

        :param rootfs_url: The rootfs_url of this GearExchange.  # noqa: E501
        :type: str
        """

        self._rootfs_url = rootfs_url


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
        if not isinstance(other, GearExchange):
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
