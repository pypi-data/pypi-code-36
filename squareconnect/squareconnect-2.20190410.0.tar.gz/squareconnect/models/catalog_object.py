# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class CatalogObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, id=None, updated_at=None, version=None, is_deleted=None, catalog_v1_ids=None, present_at_all_locations=None, present_at_location_ids=None, absent_at_location_ids=None, image_id=None, item_data=None, category_data=None, item_variation_data=None, tax_data=None, discount_data=None, modifier_list_data=None, modifier_data=None, image_data=None):
        """
        CatalogObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'updated_at': 'str',
            'version': 'int',
            'is_deleted': 'bool',
            'catalog_v1_ids': 'list[CatalogV1Id]',
            'present_at_all_locations': 'bool',
            'present_at_location_ids': 'list[str]',
            'absent_at_location_ids': 'list[str]',
            'image_id': 'str',
            'item_data': 'CatalogItem',
            'category_data': 'CatalogCategory',
            'item_variation_data': 'CatalogItemVariation',
            'tax_data': 'CatalogTax',
            'discount_data': 'CatalogDiscount',
            'modifier_list_data': 'CatalogModifierList',
            'modifier_data': 'CatalogModifier',
            'image_data': 'CatalogImage'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'updated_at': 'updated_at',
            'version': 'version',
            'is_deleted': 'is_deleted',
            'catalog_v1_ids': 'catalog_v1_ids',
            'present_at_all_locations': 'present_at_all_locations',
            'present_at_location_ids': 'present_at_location_ids',
            'absent_at_location_ids': 'absent_at_location_ids',
            'image_id': 'image_id',
            'item_data': 'item_data',
            'category_data': 'category_data',
            'item_variation_data': 'item_variation_data',
            'tax_data': 'tax_data',
            'discount_data': 'discount_data',
            'modifier_list_data': 'modifier_list_data',
            'modifier_data': 'modifier_data',
            'image_data': 'image_data'
        }

        self._type = type
        self._id = id
        self._updated_at = updated_at
        self._version = version
        self._is_deleted = is_deleted
        self._catalog_v1_ids = catalog_v1_ids
        self._present_at_all_locations = present_at_all_locations
        self._present_at_location_ids = present_at_location_ids
        self._absent_at_location_ids = absent_at_location_ids
        self._image_id = image_id
        self._item_data = item_data
        self._category_data = category_data
        self._item_variation_data = item_variation_data
        self._tax_data = tax_data
        self._discount_data = discount_data
        self._modifier_list_data = modifier_list_data
        self._modifier_data = modifier_data
        self._image_data = image_data

    @property
    def type(self):
        """
        Gets the type of this CatalogObject.
        The type of this object. Each object type has expected properties expressed in a structured format within its corresponding `*_data` field below. See [CatalogObjectType](#type-catalogobjecttype) for possible values

        :return: The type of this CatalogObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CatalogObject.
        The type of this object. Each object type has expected properties expressed in a structured format within its corresponding `*_data` field below. See [CatalogObjectType](#type-catalogobjecttype) for possible values

        :param type: The type of this CatalogObject.
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this CatalogObject.
        An identifier to reference this object in the catalog. When a new CatalogObject is inserted, the client should set the id to a temporary identifier starting with a `'#'` character. Other objects being inserted or updated within the same request may use this identifier to refer to the new object.  When the server receives the new object, it will supply a unique identifier that replaces the temporary identifier for all future references.

        :return: The id of this CatalogObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CatalogObject.
        An identifier to reference this object in the catalog. When a new CatalogObject is inserted, the client should set the id to a temporary identifier starting with a `'#'` character. Other objects being inserted or updated within the same request may use this identifier to refer to the new object.  When the server receives the new object, it will supply a unique identifier that replaces the temporary identifier for all future references.

        :param id: The id of this CatalogObject.
        :type: str
        """

        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CatalogObject.
        Last modification [timestamp](#workingwithdates) in RFC 3339 format, e.g., `\"2016-08-15T23:59:33.123Z\"` would indicate the UTC time (denoted by `Z`) of August 15, 2016 at 23:59:33 and 123 milliseconds.

        :return: The updated_at of this CatalogObject.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CatalogObject.
        Last modification [timestamp](#workingwithdates) in RFC 3339 format, e.g., `\"2016-08-15T23:59:33.123Z\"` would indicate the UTC time (denoted by `Z`) of August 15, 2016 at 23:59:33 and 123 milliseconds.

        :param updated_at: The updated_at of this CatalogObject.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def version(self):
        """
        Gets the version of this CatalogObject.
        The version of the object. When updating an object, the version supplied by the must match the version in the database, otherwise the write will be rejected as conflicting.

        :return: The version of this CatalogObject.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CatalogObject.
        The version of the object. When updating an object, the version supplied by the must match the version in the database, otherwise the write will be rejected as conflicting.

        :param version: The version of this CatalogObject.
        :type: int
        """

        self._version = version

    @property
    def is_deleted(self):
        """
        Gets the is_deleted of this CatalogObject.
        If `true`, the object has been deleted from the database. Must be `false` for new objects being inserted. When deleted, the `updated_at` field will equal the deletion time.

        :return: The is_deleted of this CatalogObject.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """
        Sets the is_deleted of this CatalogObject.
        If `true`, the object has been deleted from the database. Must be `false` for new objects being inserted. When deleted, the `updated_at` field will equal the deletion time.

        :param is_deleted: The is_deleted of this CatalogObject.
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def catalog_v1_ids(self):
        """
        Gets the catalog_v1_ids of this CatalogObject.
        The Connect V1 IDs for this object at each [location](#type-location) where it is present, where they differ from the object's Connect V2 ID. The field will only be present for objects that have been created or modified by legacy APIs.

        :return: The catalog_v1_ids of this CatalogObject.
        :rtype: list[CatalogV1Id]
        """
        return self._catalog_v1_ids

    @catalog_v1_ids.setter
    def catalog_v1_ids(self, catalog_v1_ids):
        """
        Sets the catalog_v1_ids of this CatalogObject.
        The Connect V1 IDs for this object at each [location](#type-location) where it is present, where they differ from the object's Connect V2 ID. The field will only be present for objects that have been created or modified by legacy APIs.

        :param catalog_v1_ids: The catalog_v1_ids of this CatalogObject.
        :type: list[CatalogV1Id]
        """

        self._catalog_v1_ids = catalog_v1_ids

    @property
    def present_at_all_locations(self):
        """
        Gets the present_at_all_locations of this CatalogObject.
        If `true`, this object is present at all locations (including future locations), except where specified in the `absent_at_location_ids` field. If `false`, this object is not present at any locations (including future locations), except where specified in the `present_at_location_ids` field. If not specified, defaults to `true`.

        :return: The present_at_all_locations of this CatalogObject.
        :rtype: bool
        """
        return self._present_at_all_locations

    @present_at_all_locations.setter
    def present_at_all_locations(self, present_at_all_locations):
        """
        Sets the present_at_all_locations of this CatalogObject.
        If `true`, this object is present at all locations (including future locations), except where specified in the `absent_at_location_ids` field. If `false`, this object is not present at any locations (including future locations), except where specified in the `present_at_location_ids` field. If not specified, defaults to `true`.

        :param present_at_all_locations: The present_at_all_locations of this CatalogObject.
        :type: bool
        """

        self._present_at_all_locations = present_at_all_locations

    @property
    def present_at_location_ids(self):
        """
        Gets the present_at_location_ids of this CatalogObject.
        A list of locations where the object is present, even if `present_at_all_locations` is `false`.

        :return: The present_at_location_ids of this CatalogObject.
        :rtype: list[str]
        """
        return self._present_at_location_ids

    @present_at_location_ids.setter
    def present_at_location_ids(self, present_at_location_ids):
        """
        Sets the present_at_location_ids of this CatalogObject.
        A list of locations where the object is present, even if `present_at_all_locations` is `false`.

        :param present_at_location_ids: The present_at_location_ids of this CatalogObject.
        :type: list[str]
        """

        self._present_at_location_ids = present_at_location_ids

    @property
    def absent_at_location_ids(self):
        """
        Gets the absent_at_location_ids of this CatalogObject.
        A list of locations where the object is not present, even if `present_at_all_locations` is `true`.

        :return: The absent_at_location_ids of this CatalogObject.
        :rtype: list[str]
        """
        return self._absent_at_location_ids

    @absent_at_location_ids.setter
    def absent_at_location_ids(self, absent_at_location_ids):
        """
        Sets the absent_at_location_ids of this CatalogObject.
        A list of locations where the object is not present, even if `present_at_all_locations` is `true`.

        :param absent_at_location_ids: The absent_at_location_ids of this CatalogObject.
        :type: list[str]
        """

        self._absent_at_location_ids = absent_at_location_ids

    @property
    def image_id(self):
        """
        Gets the image_id of this CatalogObject.
        Identifies the `CatalogImage` attached to this `CatalogObject`.

        :return: The image_id of this CatalogObject.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this CatalogObject.
        Identifies the `CatalogImage` attached to this `CatalogObject`.

        :param image_id: The image_id of this CatalogObject.
        :type: str
        """

        self._image_id = image_id

    @property
    def item_data(self):
        """
        Gets the item_data of this CatalogObject.
        Structured data for a [CatalogItem](#type-catalogitem), set for CatalogObjects of type `ITEM`.

        :return: The item_data of this CatalogObject.
        :rtype: CatalogItem
        """
        return self._item_data

    @item_data.setter
    def item_data(self, item_data):
        """
        Sets the item_data of this CatalogObject.
        Structured data for a [CatalogItem](#type-catalogitem), set for CatalogObjects of type `ITEM`.

        :param item_data: The item_data of this CatalogObject.
        :type: CatalogItem
        """

        self._item_data = item_data

    @property
    def category_data(self):
        """
        Gets the category_data of this CatalogObject.
        Structured data for a [CatalogCategory](#type-catalogcategory), set for CatalogObjects of type `CATEGORY`.

        :return: The category_data of this CatalogObject.
        :rtype: CatalogCategory
        """
        return self._category_data

    @category_data.setter
    def category_data(self, category_data):
        """
        Sets the category_data of this CatalogObject.
        Structured data for a [CatalogCategory](#type-catalogcategory), set for CatalogObjects of type `CATEGORY`.

        :param category_data: The category_data of this CatalogObject.
        :type: CatalogCategory
        """

        self._category_data = category_data

    @property
    def item_variation_data(self):
        """
        Gets the item_variation_data of this CatalogObject.
        Structured data for a [CatalogItemVariation](#type-catalogitemvariation), set for CatalogObjects of type `ITEM_VARIATION`.

        :return: The item_variation_data of this CatalogObject.
        :rtype: CatalogItemVariation
        """
        return self._item_variation_data

    @item_variation_data.setter
    def item_variation_data(self, item_variation_data):
        """
        Sets the item_variation_data of this CatalogObject.
        Structured data for a [CatalogItemVariation](#type-catalogitemvariation), set for CatalogObjects of type `ITEM_VARIATION`.

        :param item_variation_data: The item_variation_data of this CatalogObject.
        :type: CatalogItemVariation
        """

        self._item_variation_data = item_variation_data

    @property
    def tax_data(self):
        """
        Gets the tax_data of this CatalogObject.
        Structured data for a [CatalogTax](#type-catalogtax), set for CatalogObjects of type `TAX`.

        :return: The tax_data of this CatalogObject.
        :rtype: CatalogTax
        """
        return self._tax_data

    @tax_data.setter
    def tax_data(self, tax_data):
        """
        Sets the tax_data of this CatalogObject.
        Structured data for a [CatalogTax](#type-catalogtax), set for CatalogObjects of type `TAX`.

        :param tax_data: The tax_data of this CatalogObject.
        :type: CatalogTax
        """

        self._tax_data = tax_data

    @property
    def discount_data(self):
        """
        Gets the discount_data of this CatalogObject.
        Structured data for a [CatalogDiscount](#type-catalogdiscount), set for CatalogObjects of type `DISCOUNT`.

        :return: The discount_data of this CatalogObject.
        :rtype: CatalogDiscount
        """
        return self._discount_data

    @discount_data.setter
    def discount_data(self, discount_data):
        """
        Sets the discount_data of this CatalogObject.
        Structured data for a [CatalogDiscount](#type-catalogdiscount), set for CatalogObjects of type `DISCOUNT`.

        :param discount_data: The discount_data of this CatalogObject.
        :type: CatalogDiscount
        """

        self._discount_data = discount_data

    @property
    def modifier_list_data(self):
        """
        Gets the modifier_list_data of this CatalogObject.
        Structured data for a [CatalogModifierList](#type-catalogmodifierlist), set for CatalogObjects of type `MODIFIER_LIST`.

        :return: The modifier_list_data of this CatalogObject.
        :rtype: CatalogModifierList
        """
        return self._modifier_list_data

    @modifier_list_data.setter
    def modifier_list_data(self, modifier_list_data):
        """
        Sets the modifier_list_data of this CatalogObject.
        Structured data for a [CatalogModifierList](#type-catalogmodifierlist), set for CatalogObjects of type `MODIFIER_LIST`.

        :param modifier_list_data: The modifier_list_data of this CatalogObject.
        :type: CatalogModifierList
        """

        self._modifier_list_data = modifier_list_data

    @property
    def modifier_data(self):
        """
        Gets the modifier_data of this CatalogObject.
        Structured data for a [CatalogModifier](#type-catalogmodifier), set for CatalogObjects of type `MODIFIER`.

        :return: The modifier_data of this CatalogObject.
        :rtype: CatalogModifier
        """
        return self._modifier_data

    @modifier_data.setter
    def modifier_data(self, modifier_data):
        """
        Sets the modifier_data of this CatalogObject.
        Structured data for a [CatalogModifier](#type-catalogmodifier), set for CatalogObjects of type `MODIFIER`.

        :param modifier_data: The modifier_data of this CatalogObject.
        :type: CatalogModifier
        """

        self._modifier_data = modifier_data

    @property
    def image_data(self):
        """
        Gets the image_data of this CatalogObject.
        Structured data for a [CatalogImage](#type-catalogimage), set for CatalogObjects of type `IMAGE`.

        :return: The image_data of this CatalogObject.
        :rtype: CatalogImage
        """
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        """
        Sets the image_data of this CatalogObject.
        Structured data for a [CatalogImage](#type-catalogimage), set for CatalogObjects of type `IMAGE`.

        :param image_data: The image_data of this CatalogObject.
        :type: CatalogImage
        """

        self._image_data = image_data

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
