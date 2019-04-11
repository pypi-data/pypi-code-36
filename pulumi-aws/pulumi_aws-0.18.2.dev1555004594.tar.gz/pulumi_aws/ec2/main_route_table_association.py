# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class MainRouteTableAssociation(pulumi.CustomResource):
    original_route_table_id: pulumi.Output[str]
    """
    Used internally, see __Notes__ below
    """
    route_table_id: pulumi.Output[str]
    """
    The ID of the Route Table to set as the new
    main route table for the target VPC
    """
    vpc_id: pulumi.Output[str]
    """
    The ID of the VPC whose main route table should be set
    """
    def __init__(__self__, resource_name, opts=None, route_table_id=None, vpc_id=None, __name__=None, __opts__=None):
        """
        Provides a resource for managing the main routing table of a VPC.
        
        ## Notes
        
        On VPC creation, the AWS API always creates an initial Main Route Table. This
        resource records the ID of that Route Table under `original_route_table_id`.
        The "Delete" action for a `main_route_table_association` consists of resetting
        this original table as the Main Route Table for the VPC. You'll see this
        additional Route Table in the AWS console; it must remain intact in order for
        the `main_route_table_association` delete to work properly.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] route_table_id: The ID of the Route Table to set as the new
               main route table for the target VPC
        :param pulumi.Input[str] vpc_id: The ID of the VPC whose main route table should be set
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

        if route_table_id is None:
            raise TypeError('Missing required property route_table_id')
        __props__['route_table_id'] = route_table_id

        if vpc_id is None:
            raise TypeError('Missing required property vpc_id')
        __props__['vpc_id'] = vpc_id

        __props__['original_route_table_id'] = None

        super(MainRouteTableAssociation, __self__).__init__(
            'aws:ec2/mainRouteTableAssociation:MainRouteTableAssociation',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

