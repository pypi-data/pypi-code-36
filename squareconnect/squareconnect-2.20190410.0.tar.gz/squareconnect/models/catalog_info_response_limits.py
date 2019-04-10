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


class CatalogInfoResponseLimits(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, batch_upsert_max_objects_per_batch=None, batch_upsert_max_total_objects=None, batch_retrieve_max_object_ids=None, search_max_page_limit=None, batch_delete_max_object_ids=None, update_item_taxes_max_item_ids=None, update_item_taxes_max_taxes_to_enable=None, update_item_taxes_max_taxes_to_disable=None, update_item_modifier_lists_max_item_ids=None, update_item_modifier_lists_max_modifier_lists_to_enable=None, update_item_modifier_lists_max_modifier_lists_to_disable=None):
        """
        CatalogInfoResponseLimits - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'batch_upsert_max_objects_per_batch': 'int',
            'batch_upsert_max_total_objects': 'int',
            'batch_retrieve_max_object_ids': 'int',
            'search_max_page_limit': 'int',
            'batch_delete_max_object_ids': 'int',
            'update_item_taxes_max_item_ids': 'int',
            'update_item_taxes_max_taxes_to_enable': 'int',
            'update_item_taxes_max_taxes_to_disable': 'int',
            'update_item_modifier_lists_max_item_ids': 'int',
            'update_item_modifier_lists_max_modifier_lists_to_enable': 'int',
            'update_item_modifier_lists_max_modifier_lists_to_disable': 'int'
        }

        self.attribute_map = {
            'batch_upsert_max_objects_per_batch': 'batch_upsert_max_objects_per_batch',
            'batch_upsert_max_total_objects': 'batch_upsert_max_total_objects',
            'batch_retrieve_max_object_ids': 'batch_retrieve_max_object_ids',
            'search_max_page_limit': 'search_max_page_limit',
            'batch_delete_max_object_ids': 'batch_delete_max_object_ids',
            'update_item_taxes_max_item_ids': 'update_item_taxes_max_item_ids',
            'update_item_taxes_max_taxes_to_enable': 'update_item_taxes_max_taxes_to_enable',
            'update_item_taxes_max_taxes_to_disable': 'update_item_taxes_max_taxes_to_disable',
            'update_item_modifier_lists_max_item_ids': 'update_item_modifier_lists_max_item_ids',
            'update_item_modifier_lists_max_modifier_lists_to_enable': 'update_item_modifier_lists_max_modifier_lists_to_enable',
            'update_item_modifier_lists_max_modifier_lists_to_disable': 'update_item_modifier_lists_max_modifier_lists_to_disable'
        }

        self._batch_upsert_max_objects_per_batch = batch_upsert_max_objects_per_batch
        self._batch_upsert_max_total_objects = batch_upsert_max_total_objects
        self._batch_retrieve_max_object_ids = batch_retrieve_max_object_ids
        self._search_max_page_limit = search_max_page_limit
        self._batch_delete_max_object_ids = batch_delete_max_object_ids
        self._update_item_taxes_max_item_ids = update_item_taxes_max_item_ids
        self._update_item_taxes_max_taxes_to_enable = update_item_taxes_max_taxes_to_enable
        self._update_item_taxes_max_taxes_to_disable = update_item_taxes_max_taxes_to_disable
        self._update_item_modifier_lists_max_item_ids = update_item_modifier_lists_max_item_ids
        self._update_item_modifier_lists_max_modifier_lists_to_enable = update_item_modifier_lists_max_modifier_lists_to_enable
        self._update_item_modifier_lists_max_modifier_lists_to_disable = update_item_modifier_lists_max_modifier_lists_to_disable

    @property
    def batch_upsert_max_objects_per_batch(self):
        """
        Gets the batch_upsert_max_objects_per_batch of this CatalogInfoResponseLimits.
        The maximum number of objects that may appear within a single batch in a `/v2/catalog/batch-upsert` request.

        :return: The batch_upsert_max_objects_per_batch of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._batch_upsert_max_objects_per_batch

    @batch_upsert_max_objects_per_batch.setter
    def batch_upsert_max_objects_per_batch(self, batch_upsert_max_objects_per_batch):
        """
        Sets the batch_upsert_max_objects_per_batch of this CatalogInfoResponseLimits.
        The maximum number of objects that may appear within a single batch in a `/v2/catalog/batch-upsert` request.

        :param batch_upsert_max_objects_per_batch: The batch_upsert_max_objects_per_batch of this CatalogInfoResponseLimits.
        :type: int
        """

        self._batch_upsert_max_objects_per_batch = batch_upsert_max_objects_per_batch

    @property
    def batch_upsert_max_total_objects(self):
        """
        Gets the batch_upsert_max_total_objects of this CatalogInfoResponseLimits.
        The maximum number of objects that may appear across all batches in a `/v2/catalog/batch-upsert` request.

        :return: The batch_upsert_max_total_objects of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._batch_upsert_max_total_objects

    @batch_upsert_max_total_objects.setter
    def batch_upsert_max_total_objects(self, batch_upsert_max_total_objects):
        """
        Sets the batch_upsert_max_total_objects of this CatalogInfoResponseLimits.
        The maximum number of objects that may appear across all batches in a `/v2/catalog/batch-upsert` request.

        :param batch_upsert_max_total_objects: The batch_upsert_max_total_objects of this CatalogInfoResponseLimits.
        :type: int
        """

        self._batch_upsert_max_total_objects = batch_upsert_max_total_objects

    @property
    def batch_retrieve_max_object_ids(self):
        """
        Gets the batch_retrieve_max_object_ids of this CatalogInfoResponseLimits.
        The maximum number of object IDs that may appear in a `/v2/catalog/batch-retrieve` request.

        :return: The batch_retrieve_max_object_ids of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._batch_retrieve_max_object_ids

    @batch_retrieve_max_object_ids.setter
    def batch_retrieve_max_object_ids(self, batch_retrieve_max_object_ids):
        """
        Sets the batch_retrieve_max_object_ids of this CatalogInfoResponseLimits.
        The maximum number of object IDs that may appear in a `/v2/catalog/batch-retrieve` request.

        :param batch_retrieve_max_object_ids: The batch_retrieve_max_object_ids of this CatalogInfoResponseLimits.
        :type: int
        """

        self._batch_retrieve_max_object_ids = batch_retrieve_max_object_ids

    @property
    def search_max_page_limit(self):
        """
        Gets the search_max_page_limit of this CatalogInfoResponseLimits.
        The maximum number of results that may be returned in a page of a `/v2/catalog/search` response.

        :return: The search_max_page_limit of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._search_max_page_limit

    @search_max_page_limit.setter
    def search_max_page_limit(self, search_max_page_limit):
        """
        Sets the search_max_page_limit of this CatalogInfoResponseLimits.
        The maximum number of results that may be returned in a page of a `/v2/catalog/search` response.

        :param search_max_page_limit: The search_max_page_limit of this CatalogInfoResponseLimits.
        :type: int
        """

        self._search_max_page_limit = search_max_page_limit

    @property
    def batch_delete_max_object_ids(self):
        """
        Gets the batch_delete_max_object_ids of this CatalogInfoResponseLimits.
        The maximum number of object IDs that may be included in a single `/v2/catalog/batch-delete` request.

        :return: The batch_delete_max_object_ids of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._batch_delete_max_object_ids

    @batch_delete_max_object_ids.setter
    def batch_delete_max_object_ids(self, batch_delete_max_object_ids):
        """
        Sets the batch_delete_max_object_ids of this CatalogInfoResponseLimits.
        The maximum number of object IDs that may be included in a single `/v2/catalog/batch-delete` request.

        :param batch_delete_max_object_ids: The batch_delete_max_object_ids of this CatalogInfoResponseLimits.
        :type: int
        """

        self._batch_delete_max_object_ids = batch_delete_max_object_ids

    @property
    def update_item_taxes_max_item_ids(self):
        """
        Gets the update_item_taxes_max_item_ids of this CatalogInfoResponseLimits.
        The maximum number of item IDs that may be included in a single `/v2/catalog/update-item-taxes` request.

        :return: The update_item_taxes_max_item_ids of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._update_item_taxes_max_item_ids

    @update_item_taxes_max_item_ids.setter
    def update_item_taxes_max_item_ids(self, update_item_taxes_max_item_ids):
        """
        Sets the update_item_taxes_max_item_ids of this CatalogInfoResponseLimits.
        The maximum number of item IDs that may be included in a single `/v2/catalog/update-item-taxes` request.

        :param update_item_taxes_max_item_ids: The update_item_taxes_max_item_ids of this CatalogInfoResponseLimits.
        :type: int
        """

        self._update_item_taxes_max_item_ids = update_item_taxes_max_item_ids

    @property
    def update_item_taxes_max_taxes_to_enable(self):
        """
        Gets the update_item_taxes_max_taxes_to_enable of this CatalogInfoResponseLimits.
        The maximum number of tax IDs to be enabled that may be included in a single `/v2/catalog/update-item-taxes` request.

        :return: The update_item_taxes_max_taxes_to_enable of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._update_item_taxes_max_taxes_to_enable

    @update_item_taxes_max_taxes_to_enable.setter
    def update_item_taxes_max_taxes_to_enable(self, update_item_taxes_max_taxes_to_enable):
        """
        Sets the update_item_taxes_max_taxes_to_enable of this CatalogInfoResponseLimits.
        The maximum number of tax IDs to be enabled that may be included in a single `/v2/catalog/update-item-taxes` request.

        :param update_item_taxes_max_taxes_to_enable: The update_item_taxes_max_taxes_to_enable of this CatalogInfoResponseLimits.
        :type: int
        """

        self._update_item_taxes_max_taxes_to_enable = update_item_taxes_max_taxes_to_enable

    @property
    def update_item_taxes_max_taxes_to_disable(self):
        """
        Gets the update_item_taxes_max_taxes_to_disable of this CatalogInfoResponseLimits.
        The maximum number of tax IDs to be disabled that may be included in a single `/v2/catalog/update-item-taxes` request.

        :return: The update_item_taxes_max_taxes_to_disable of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._update_item_taxes_max_taxes_to_disable

    @update_item_taxes_max_taxes_to_disable.setter
    def update_item_taxes_max_taxes_to_disable(self, update_item_taxes_max_taxes_to_disable):
        """
        Sets the update_item_taxes_max_taxes_to_disable of this CatalogInfoResponseLimits.
        The maximum number of tax IDs to be disabled that may be included in a single `/v2/catalog/update-item-taxes` request.

        :param update_item_taxes_max_taxes_to_disable: The update_item_taxes_max_taxes_to_disable of this CatalogInfoResponseLimits.
        :type: int
        """

        self._update_item_taxes_max_taxes_to_disable = update_item_taxes_max_taxes_to_disable

    @property
    def update_item_modifier_lists_max_item_ids(self):
        """
        Gets the update_item_modifier_lists_max_item_ids of this CatalogInfoResponseLimits.
        The maximum number of item IDs that may be included in a single `/v2/catalog/update-item-modifier-lists` request.

        :return: The update_item_modifier_lists_max_item_ids of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._update_item_modifier_lists_max_item_ids

    @update_item_modifier_lists_max_item_ids.setter
    def update_item_modifier_lists_max_item_ids(self, update_item_modifier_lists_max_item_ids):
        """
        Sets the update_item_modifier_lists_max_item_ids of this CatalogInfoResponseLimits.
        The maximum number of item IDs that may be included in a single `/v2/catalog/update-item-modifier-lists` request.

        :param update_item_modifier_lists_max_item_ids: The update_item_modifier_lists_max_item_ids of this CatalogInfoResponseLimits.
        :type: int
        """

        self._update_item_modifier_lists_max_item_ids = update_item_modifier_lists_max_item_ids

    @property
    def update_item_modifier_lists_max_modifier_lists_to_enable(self):
        """
        Gets the update_item_modifier_lists_max_modifier_lists_to_enable of this CatalogInfoResponseLimits.
        The maximum number of modifier list IDs to be enabled that may be included in a single `/v2/catalog/update-item-modifier-lists` request.

        :return: The update_item_modifier_lists_max_modifier_lists_to_enable of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._update_item_modifier_lists_max_modifier_lists_to_enable

    @update_item_modifier_lists_max_modifier_lists_to_enable.setter
    def update_item_modifier_lists_max_modifier_lists_to_enable(self, update_item_modifier_lists_max_modifier_lists_to_enable):
        """
        Sets the update_item_modifier_lists_max_modifier_lists_to_enable of this CatalogInfoResponseLimits.
        The maximum number of modifier list IDs to be enabled that may be included in a single `/v2/catalog/update-item-modifier-lists` request.

        :param update_item_modifier_lists_max_modifier_lists_to_enable: The update_item_modifier_lists_max_modifier_lists_to_enable of this CatalogInfoResponseLimits.
        :type: int
        """

        self._update_item_modifier_lists_max_modifier_lists_to_enable = update_item_modifier_lists_max_modifier_lists_to_enable

    @property
    def update_item_modifier_lists_max_modifier_lists_to_disable(self):
        """
        Gets the update_item_modifier_lists_max_modifier_lists_to_disable of this CatalogInfoResponseLimits.
        The maximum number of modifier list IDs to be disabled that may be included in a single `/v2/catalog/update-item-modifier-lists` request.

        :return: The update_item_modifier_lists_max_modifier_lists_to_disable of this CatalogInfoResponseLimits.
        :rtype: int
        """
        return self._update_item_modifier_lists_max_modifier_lists_to_disable

    @update_item_modifier_lists_max_modifier_lists_to_disable.setter
    def update_item_modifier_lists_max_modifier_lists_to_disable(self, update_item_modifier_lists_max_modifier_lists_to_disable):
        """
        Sets the update_item_modifier_lists_max_modifier_lists_to_disable of this CatalogInfoResponseLimits.
        The maximum number of modifier list IDs to be disabled that may be included in a single `/v2/catalog/update-item-modifier-lists` request.

        :param update_item_modifier_lists_max_modifier_lists_to_disable: The update_item_modifier_lists_max_modifier_lists_to_disable of this CatalogInfoResponseLimits.
        :type: int
        """

        self._update_item_modifier_lists_max_modifier_lists_to_disable = update_item_modifier_lists_max_modifier_lists_to_disable

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
