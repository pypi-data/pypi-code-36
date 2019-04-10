# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.3), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.3
    Contact: info@purestorage.com
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


class ArraysApi(object):
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

    def list_arrays(self, **kwargs):
        """
        List arrays
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ArrayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_arrays_with_http_info(**kwargs)
        else:
            (data) = self.list_arrays_with_http_info(**kwargs)
            return data

    def list_arrays_with_http_info(self, **kwargs):
        """
        List arrays
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ArrayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_arrays" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.3/arrays', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ArrayResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_arrays_http_specific_performance(self, **kwargs):
        """
        List instant or historical http specific performance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_http_specific_performance(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :return: ArrayHttpPerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_arrays_http_specific_performance_with_http_info(**kwargs)
        else:
            (data) = self.list_arrays_http_specific_performance_with_http_info(**kwargs)
            return data

    def list_arrays_http_specific_performance_with_http_info(self, **kwargs):
        """
        List instant or historical http specific performance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_http_specific_performance_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :return: ArrayHttpPerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'resolution']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_arrays_http_specific_performance" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))

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
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.3/arrays/http-specific-performance', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ArrayHttpPerformanceResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_arrays_performance(self, **kwargs):
        """
        List instant or historical array performance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_performance(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :param str protocol: to sample performance of a certain protocol
        :return: ArrayPerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_arrays_performance_with_http_info(**kwargs)
        else:
            (data) = self.list_arrays_performance_with_http_info(**kwargs)
            return data

    def list_arrays_performance_with_http_info(self, **kwargs):
        """
        List instant or historical array performance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_performance_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :param str protocol: to sample performance of a certain protocol
        :return: ArrayPerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'resolution', 'protocol']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_arrays_performance" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'protocol' in params:
            query_params.append(('protocol', params['protocol']))

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
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.3/arrays/performance', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ArrayPerformanceResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_arrays_s3_specific_performance(self, **kwargs):
        """
        List instant or historical object store specific performance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_s3_specific_performance(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :return: ArrayS3PerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_arrays_s3_specific_performance_with_http_info(**kwargs)
        else:
            (data) = self.list_arrays_s3_specific_performance_with_http_info(**kwargs)
            return data

    def list_arrays_s3_specific_performance_with_http_info(self, **kwargs):
        """
        List instant or historical object store specific performance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_s3_specific_performance_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :return: ArrayS3PerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'resolution']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_arrays_s3_specific_performance" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))

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
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.3/arrays/s3-specific-performance', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ArrayS3PerformanceResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_arrays_space(self, **kwargs):
        """
        List instant or historical array space
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_space(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :param str type: to sample space of either file systems or object store
        :return: ArraySpaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_arrays_space_with_http_info(**kwargs)
        else:
            (data) = self.list_arrays_space_with_http_info(**kwargs)
            return data

    def list_arrays_space_with_http_info(self, **kwargs):
        """
        List instant or historical array space
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_arrays_space_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: Time to start sample in milliseconds since epoch.
        :param int end_time: Time to end sample in milliseconds since epoch.
        :param int resolution: sample frequency in milliseconds
        :param str type: to sample space of either file systems or object store
        :return: ArraySpaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'resolution', 'type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_arrays_space" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))
        if 'resolution' in params:
            query_params.append(('resolution', params['resolution']))
        if 'type' in params:
            query_params.append(('type', params['type']))

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
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.3/arrays/space', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ArraySpaceResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_arrays(self, array_settings, **kwargs):
        """
        Update arrays
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_arrays(array_settings, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PureArray array_settings: (required)
        :return: ArrayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_arrays_with_http_info(array_settings, **kwargs)
        else:
            (data) = self.update_arrays_with_http_info(array_settings, **kwargs)
            return data

    def update_arrays_with_http_info(self, array_settings, **kwargs):
        """
        Update arrays
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_arrays_with_http_info(array_settings, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PureArray array_settings: (required)
        :return: ArrayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['array_settings']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_arrays" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'array_settings' is set
        if ('array_settings' not in params) or (params['array_settings'] is None):
            raise ValueError("Missing the required parameter `array_settings` when calling `update_arrays`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'array_settings' in params:
            body_params = params['array_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.3/arrays', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ArrayResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
