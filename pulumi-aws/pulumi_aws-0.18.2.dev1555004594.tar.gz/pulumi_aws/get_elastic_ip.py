# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetElasticIpResult:
    """
    A collection of values returned by getElasticIp.
    """
    def __init__(__self__, association_id=None, domain=None, id=None, instance_id=None, network_interface_id=None, network_interface_owner_id=None, private_dns=None, private_ip=None, public_dns=None, public_ip=None, public_ipv4_pool=None, tags=None):
        if association_id and not isinstance(association_id, str):
            raise TypeError('Expected argument association_id to be a str')
        __self__.association_id = association_id
        """
        The ID representing the association of the address with an instance in a VPC.
        """
        if domain and not isinstance(domain, str):
            raise TypeError('Expected argument domain to be a str')
        __self__.domain = domain
        """
        Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.
        """
        if instance_id and not isinstance(instance_id, str):
            raise TypeError('Expected argument instance_id to be a str')
        __self__.instance_id = instance_id
        """
        The ID of the instance that the address is associated with (if any).
        """
        if network_interface_id and not isinstance(network_interface_id, str):
            raise TypeError('Expected argument network_interface_id to be a str')
        __self__.network_interface_id = network_interface_id
        """
        The ID of the network interface.
        """
        if network_interface_owner_id and not isinstance(network_interface_owner_id, str):
            raise TypeError('Expected argument network_interface_owner_id to be a str')
        __self__.network_interface_owner_id = network_interface_owner_id
        """
        The ID of the AWS account that owns the network interface.
        """
        if private_dns and not isinstance(private_dns, str):
            raise TypeError('Expected argument private_dns to be a str')
        __self__.private_dns = private_dns
        """
        The Private DNS associated with the Elastic IP address.
        """
        if private_ip and not isinstance(private_ip, str):
            raise TypeError('Expected argument private_ip to be a str')
        __self__.private_ip = private_ip
        """
        The private IP address associated with the Elastic IP address.
        """
        if public_dns and not isinstance(public_dns, str):
            raise TypeError('Expected argument public_dns to be a str')
        __self__.public_dns = public_dns
        """
        Public DNS associated with the Elastic IP address.
        """
        if public_ip and not isinstance(public_ip, str):
            raise TypeError('Expected argument public_ip to be a str')
        __self__.public_ip = public_ip
        """
        Public IP address of Elastic IP.
        """
        if public_ipv4_pool and not isinstance(public_ipv4_pool, str):
            raise TypeError('Expected argument public_ipv4_pool to be a str')
        __self__.public_ipv4_pool = public_ipv4_pool
        """
        The ID of an address pool.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        Key-value map of tags associated with Elastic IP.
        """

async def get_elastic_ip(filters=None,id=None,public_ip=None,tags=None,opts=None):
    """
    `aws_eip` provides details about a specific Elastic IP.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['id'] = id
    __args__['publicIp'] = public_ip
    __args__['tags'] = tags
    __ret__ = await pulumi.runtime.invoke('aws:index/getElasticIp:getElasticIp', __args__, opts=opts)

    return GetElasticIpResult(
        association_id=__ret__.get('associationId'),
        domain=__ret__.get('domain'),
        id=__ret__.get('id'),
        instance_id=__ret__.get('instanceId'),
        network_interface_id=__ret__.get('networkInterfaceId'),
        network_interface_owner_id=__ret__.get('networkInterfaceOwnerId'),
        private_dns=__ret__.get('privateDns'),
        private_ip=__ret__.get('privateIp'),
        public_dns=__ret__.get('publicDns'),
        public_ip=__ret__.get('publicIp'),
        public_ipv4_pool=__ret__.get('publicIpv4Pool'),
        tags=__ret__.get('tags'))
