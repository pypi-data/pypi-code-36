# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Listener(pulumi.CustomResource):
    accelerator_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of your accelerator.
    """
    client_affinity: pulumi.Output[str]
    """
    Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
    """
    port_ranges: pulumi.Output[list]
    """
    The list of port ranges for the connections from clients to the accelerator. Fields documented below.
    """
    protocol: pulumi.Output[str]
    """
    The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
    """
    def __init__(__self__, resource_name, opts=None, accelerator_arn=None, client_affinity=None, port_ranges=None, protocol=None, __name__=None, __opts__=None):
        """
        Provides a Global Accelerator listener.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param pulumi.Input[str] client_affinity: Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the "five-tuple" properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the "two-tuple" properties of source (client) IP address and destination IP address to select the hash value.
        :param pulumi.Input[list] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        :param pulumi.Input[str] protocol: The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if accelerator_arn is None:
            raise TypeError('Missing required property accelerator_arn')
        __props__['accelerator_arn'] = accelerator_arn

        __props__['client_affinity'] = client_affinity

        if port_ranges is None:
            raise TypeError('Missing required property port_ranges')
        __props__['port_ranges'] = port_ranges

        if protocol is None:
            raise TypeError('Missing required property protocol')
        __props__['protocol'] = protocol

        super(Listener, __self__).__init__(
            'aws:globalaccelerator/listener:Listener',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

