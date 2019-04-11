# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class InviteAccepter(pulumi.CustomResource):
    detector_id: pulumi.Output[str]
    """
    The detector ID of the member GuardDuty account.
    """
    master_account_id: pulumi.Output[str]
    """
    AWS account ID for master account.
    """
    def __init__(__self__, resource_name, opts=None, detector_id=None, master_account_id=None, __name__=None, __opts__=None):
        """
        Provides a resource to accept a pending GuardDuty invite on creation, ensure the detector has the correct master account on read, and disassociate with the master account upon removal.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for master account.
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

        if detector_id is None:
            raise TypeError('Missing required property detector_id')
        __props__['detector_id'] = detector_id

        if master_account_id is None:
            raise TypeError('Missing required property master_account_id')
        __props__['master_account_id'] = master_account_id

        super(InviteAccepter, __self__).__init__(
            'aws:guardduty/inviteAccepter:InviteAccepter',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

