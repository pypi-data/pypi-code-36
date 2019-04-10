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

from flywheel.models.avatars import Avatars  # noqa: F401,E501
from flywheel.models.user_api_key import UserApiKey  # noqa: F401,E501
from flywheel.models.user_preferences import UserPreferences  # noqa: F401,E501
from flywheel.models.user_wechat import UserWechat  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class User(object):

    swagger_types = {
        'id': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'avatar': 'str',
        'avatars': 'Avatars',
        'root': 'bool',
        'disabled': 'bool',
        'preferences': 'UserPreferences',
        'wechat': 'UserWechat',
        'firstlogin': 'str',
        'lastlogin': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'api_key': 'UserApiKey'
    }

    attribute_map = {
        'id': '_id',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'avatar': 'avatar',
        'avatars': 'avatars',
        'root': 'root',
        'disabled': 'disabled',
        'preferences': 'preferences',
        'wechat': 'wechat',
        'firstlogin': 'firstlogin',
        'lastlogin': 'lastlogin',
        'created': 'created',
        'modified': 'modified',
        'api_key': 'api_key'
    }

    rattribute_map = {
        '_id': 'id',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'avatar': 'avatar',
        'avatars': 'avatars',
        'root': 'root',
        'disabled': 'disabled',
        'preferences': 'preferences',
        'wechat': 'wechat',
        'firstlogin': 'firstlogin',
        'lastlogin': 'lastlogin',
        'created': 'created',
        'modified': 'modified',
        'api_key': 'api_key'
    }

    def __init__(self, id=None, firstname=None, lastname=None, email=None, avatar=None, avatars=None, root=None, disabled=None, preferences=None, wechat=None, firstlogin=None, lastlogin=None, created=None, modified=None, api_key=None):  # noqa: E501
        """User - a model defined in Swagger"""
        super(User, self).__init__()

        self._id = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._avatar = None
        self._avatars = None
        self._root = None
        self._disabled = None
        self._preferences = None
        self._wechat = None
        self._firstlogin = None
        self._lastlogin = None
        self._created = None
        self._modified = None
        self._api_key = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if avatar is not None:
            self.avatar = avatar
        if avatars is not None:
            self.avatars = avatars
        if root is not None:
            self.root = root
        if disabled is not None:
            self.disabled = disabled
        if preferences is not None:
            self.preferences = preferences
        if wechat is not None:
            self.wechat = wechat
        if firstlogin is not None:
            self.firstlogin = firstlogin
        if lastlogin is not None:
            self.lastlogin = lastlogin
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if api_key is not None:
            self.api_key = api_key

    @property
    def id(self):
        """Gets the id of this User.

        Database ID of a user

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        Database ID of a user

        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def firstname(self):
        """Gets the firstname of this User.

        First name

        :return: The firstname of this User.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this User.

        First name

        :param firstname: The firstname of this User.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this User.

        Last name

        :return: The lastname of this User.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this User.

        Last name

        :param lastname: The lastname of this User.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this User.

        Email address

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        Email address

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def avatar(self):
        """Gets the avatar of this User.

        Avatar image URL

        :return: The avatar of this User.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this User.

        Avatar image URL

        :param avatar: The avatar of this User.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def avatars(self):
        """Gets the avatars of this User.


        :return: The avatars of this User.
        :rtype: Avatars
        """
        return self._avatars

    @avatars.setter
    def avatars(self, avatars):
        """Sets the avatars of this User.


        :param avatars: The avatars of this User.  # noqa: E501
        :type: Avatars
        """

        self._avatars = avatars

    @property
    def root(self):
        """Gets the root of this User.

        Super admin flag

        :return: The root of this User.
        :rtype: bool
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this User.

        Super admin flag

        :param root: The root of this User.  # noqa: E501
        :type: bool
        """

        self._root = root

    @property
    def disabled(self):
        """Gets the disabled of this User.


        :return: The disabled of this User.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this User.


        :param disabled: The disabled of this User.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def preferences(self):
        """Gets the preferences of this User.


        :return: The preferences of this User.
        :rtype: UserPreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this User.


        :param preferences: The preferences of this User.  # noqa: E501
        :type: UserPreferences
        """

        self._preferences = preferences

    @property
    def wechat(self):
        """Gets the wechat of this User.


        :return: The wechat of this User.
        :rtype: UserWechat
        """
        return self._wechat

    @wechat.setter
    def wechat(self, wechat):
        """Sets the wechat of this User.


        :param wechat: The wechat of this User.  # noqa: E501
        :type: UserWechat
        """

        self._wechat = wechat

    @property
    def firstlogin(self):
        """Gets the firstlogin of this User.


        :return: The firstlogin of this User.
        :rtype: str
        """
        return self._firstlogin

    @firstlogin.setter
    def firstlogin(self, firstlogin):
        """Sets the firstlogin of this User.


        :param firstlogin: The firstlogin of this User.  # noqa: E501
        :type: str
        """

        self._firstlogin = firstlogin

    @property
    def lastlogin(self):
        """Gets the lastlogin of this User.


        :return: The lastlogin of this User.
        :rtype: str
        """
        return self._lastlogin

    @lastlogin.setter
    def lastlogin(self, lastlogin):
        """Sets the lastlogin of this User.


        :param lastlogin: The lastlogin of this User.  # noqa: E501
        :type: str
        """

        self._lastlogin = lastlogin

    @property
    def created(self):
        """Gets the created of this User.

        Creation time (automatically set)

        :return: The created of this User.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this User.

        Creation time (automatically set)

        :param created: The created of this User.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this User.

        Last modification time (automatically updated)

        :return: The modified of this User.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this User.

        Last modification time (automatically updated)

        :param modified: The modified of this User.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def api_key(self):
        """Gets the api_key of this User.


        :return: The api_key of this User.
        :rtype: UserApiKey
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this User.


        :param api_key: The api_key of this User.  # noqa: E501
        :type: UserApiKey
        """

        self._api_key = api_key


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
        if not isinstance(other, User):
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
