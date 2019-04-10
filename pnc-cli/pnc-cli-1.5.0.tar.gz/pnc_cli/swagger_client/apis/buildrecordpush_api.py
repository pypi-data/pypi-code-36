# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BuildrecordpushApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cancel(self, build_record_id, **kwargs):
        """
        Build record push results.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :param BuildRecordPushResultRest body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_with_http_info(build_record_id, **kwargs)
        else:
            (data) = self.cancel_with_http_info(build_record_id, **kwargs)
            return data

    def cancel_with_http_info(self, build_record_id, **kwargs):
        """
        Build record push results.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_with_http_info(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :param BuildRecordPushResultRest body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_record_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_record_id' is set
        if ('build_record_id' not in params) or (params['build_record_id'] is None):
            raise ValueError("Missing the required parameter `build_record_id` when calling `cancel`")


        collection_formats = {}

        path_params = {}
        if 'build_record_id' in params:
            path_params['buildRecordId'] = params['build_record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/build-record-push/{buildRecordId}/cancel', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='int',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get(self, build_record_id, **kwargs):
        """
        Get Build Record Push Result by Id..
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :return: BuildRecordPushResultRest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(build_record_id, **kwargs)
        else:
            (data) = self.get_with_http_info(build_record_id, **kwargs)
            return data

    def get_with_http_info(self, build_record_id, **kwargs):
        """
        Get Build Record Push Result by Id..
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :return: BuildRecordPushResultRest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_record_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_record_id' is set
        if ('build_record_id' not in params) or (params['build_record_id'] is None):
            raise ValueError("Missing the required parameter `build_record_id` when calling `get`")


        collection_formats = {}

        path_params = {}
        if 'build_record_id' in params:
            path_params['buildRecordId'] = params['build_record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/build-record-push/{buildRecordPushResultId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BuildRecordPushResultRest',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def push(self, **kwargs):
        """
        Push build record results to Brew.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.push(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BuildRecordPushRequestRest body:
        :return: list[ResultRest]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.push_with_http_info(**kwargs)
        else:
            (data) = self.push_with_http_info(**kwargs)
            return data

    def push_with_http_info(self, **kwargs):
        """
        Push build record results to Brew.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.push_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BuildRecordPushRequestRest body:
        :return: list[ResultRest]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method push" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/build-record-push', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ResultRest]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def push_0(self, build_record_id, **kwargs):
        """
        Build record push results.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.push_0(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :param BuildRecordPushResultRest body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.push_0_with_http_info(build_record_id, **kwargs)
        else:
            (data) = self.push_0_with_http_info(build_record_id, **kwargs)
            return data

    def push_0_with_http_info(self, build_record_id, **kwargs):
        """
        Build record push results.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.push_0_with_http_info(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :param BuildRecordPushResultRest body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_record_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method push_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_record_id' is set
        if ('build_record_id' not in params) or (params['build_record_id'] is None):
            raise ValueError("Missing the required parameter `build_record_id` when calling `push_0`")


        collection_formats = {}

        path_params = {}
        if 'build_record_id' in params:
            path_params['buildRecordId'] = params['build_record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/build-record-push/{buildRecordId}/complete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='int',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def push_record_set(self, **kwargs):
        """
        Push build config set record to Brew.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.push_record_set(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BuildConfigSetRecordPushRequestRest body:
        :return: list[ResultRest]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.push_record_set_with_http_info(**kwargs)
        else:
            (data) = self.push_record_set_with_http_info(**kwargs)
            return data

    def push_record_set_with_http_info(self, **kwargs):
        """
        Push build config set record to Brew.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.push_record_set_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BuildConfigSetRecordPushRequestRest body:
        :return: list[ResultRest]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method push_record_set" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/build-record-push/record-set', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ResultRest]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def status(self, build_record_id, **kwargs):
        """
        Latest push result of BuildRecord.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.status(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :return: BuildRecordPushResultRest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.status_with_http_info(build_record_id, **kwargs)
        else:
            (data) = self.status_with_http_info(build_record_id, **kwargs)
            return data

    def status_with_http_info(self, build_record_id, **kwargs):
        """
        Latest push result of BuildRecord.
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.status_with_http_info(build_record_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int build_record_id: Build Record id (required)
        :return: BuildRecordPushResultRest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['build_record_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'build_record_id' is set
        if ('build_record_id' not in params) or (params['build_record_id'] is None):
            raise ValueError("Missing the required parameter `build_record_id` when calling `status`")


        collection_formats = {}

        path_params = {}
        if 'build_record_id' in params:
            path_params['buildRecordId'] = params['build_record_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/build-record-push/status/{buildRecordId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BuildRecordPushResultRest',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
