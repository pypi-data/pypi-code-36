# coding: utf-8

"""
    VXC Services API

    API for methods pertaining to all VXC services  # noqa: E501

    OpenAPI spec version: 1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vincrosscheck.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def vehicle_financial_portfolio_add_options(self, **kwargs):  # noqa: E501
        """vehicle_financial_portfolio_add_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.vehicle_financial_portfolio_add_options(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.vehicle_financial_portfolio_add_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.vehicle_financial_portfolio_add_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def vehicle_financial_portfolio_add_options_with_http_info(self, **kwargs):  # noqa: E501
        """vehicle_financial_portfolio_add_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.vehicle_financial_portfolio_add_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vehicle_financial_portfolio_add_options" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CustomerAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/vehicle/financial/portfolio/add', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vehicle_financial_portfolio_alerts_options(self, **kwargs):  # noqa: E501
        """vehicle_financial_portfolio_alerts_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.vehicle_financial_portfolio_alerts_options(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.vehicle_financial_portfolio_alerts_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.vehicle_financial_portfolio_alerts_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def vehicle_financial_portfolio_alerts_options_with_http_info(self, **kwargs):  # noqa: E501
        """vehicle_financial_portfolio_alerts_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.vehicle_financial_portfolio_alerts_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vehicle_financial_portfolio_alerts_options" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CustomerAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/vehicle/financial/portfolio/alerts', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vehicle_financial_portfolio_remove_options(self, **kwargs):  # noqa: E501
        """vehicle_financial_portfolio_remove_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.vehicle_financial_portfolio_remove_options(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.vehicle_financial_portfolio_remove_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.vehicle_financial_portfolio_remove_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def vehicle_financial_portfolio_remove_options_with_http_info(self, **kwargs):  # noqa: E501
        """vehicle_financial_portfolio_remove_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.vehicle_financial_portfolio_remove_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vehicle_financial_portfolio_remove_options" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CustomerAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/vehicle/financial/portfolio/remove', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_brickftp_vxc_compressed_options(self, **kwargs):  # noqa: E501
        """webhook_brickftp_vxc_compressed_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.webhook_brickftp_vxc_compressed_options(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.webhook_brickftp_vxc_compressed_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.webhook_brickftp_vxc_compressed_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def webhook_brickftp_vxc_compressed_options_with_http_info(self, **kwargs):  # noqa: E501
        """webhook_brickftp_vxc_compressed_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.webhook_brickftp_vxc_compressed_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_brickftp_vxc_compressed_options" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CustomerAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/brickftp/vxc/compressed', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_brickftp_vxc_encrypted_options(self, **kwargs):  # noqa: E501
        """webhook_brickftp_vxc_encrypted_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.webhook_brickftp_vxc_encrypted_options(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.webhook_brickftp_vxc_encrypted_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.webhook_brickftp_vxc_encrypted_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def webhook_brickftp_vxc_encrypted_options_with_http_info(self, **kwargs):  # noqa: E501
        """webhook_brickftp_vxc_encrypted_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.webhook_brickftp_vxc_encrypted_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_brickftp_vxc_encrypted_options" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CustomerAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/brickftp/vxc/encrypted', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def webhook_brickftp_vxc_options(self, **kwargs):  # noqa: E501
        """webhook_brickftp_vxc_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.webhook_brickftp_vxc_options(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.webhook_brickftp_vxc_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.webhook_brickftp_vxc_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def webhook_brickftp_vxc_options_with_http_info(self, **kwargs):  # noqa: E501
        """webhook_brickftp_vxc_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.webhook_brickftp_vxc_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webhook_brickftp_vxc_options" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CustomerAuthorizer']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/brickftp/vxc', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
