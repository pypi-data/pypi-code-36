# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Key(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the key.
    """
    deletion_window_in_days: pulumi.Output[float]
    """
    Duration in days after which the key is deleted
    after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.
    """
    description: pulumi.Output[str]
    """
    The description of the key as viewed in AWS console.
    """
    enable_key_rotation: pulumi.Output[bool]
    """
    Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
    is enabled. Defaults to false.
    """
    is_enabled: pulumi.Output[bool]
    """
    Specifies whether the key is enabled. Defaults to true.
    """
    key_id: pulumi.Output[str]
    """
    The globally unique identifier for the key.
    """
    key_usage: pulumi.Output[str]
    """
    Specifies the intended use of the key.
    Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.
    """
    policy: pulumi.Output[str]
    """
    A valid policy JSON document. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the object.
    """
    def __init__(__self__, resource_name, opts=None, deletion_window_in_days=None, description=None, enable_key_rotation=None, is_enabled=None, key_usage=None, policy=None, tags=None, __name__=None, __opts__=None):
        """
        Provides a KMS customer master key.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] deletion_window_in_days: Duration in days after which the key is deleted
               after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.
        :param pulumi.Input[str] description: The description of the key as viewed in AWS console.
        :param pulumi.Input[bool] enable_key_rotation: Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
               is enabled. Defaults to false.
        :param pulumi.Input[bool] is_enabled: Specifies whether the key is enabled. Defaults to true.
        :param pulumi.Input[str] key_usage: Specifies the intended use of the key.
               Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.
        :param pulumi.Input[str] policy: A valid policy JSON document. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the object.
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

        __props__['deletion_window_in_days'] = deletion_window_in_days

        __props__['description'] = description

        __props__['enable_key_rotation'] = enable_key_rotation

        __props__['is_enabled'] = is_enabled

        __props__['key_usage'] = key_usage

        __props__['policy'] = policy

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['key_id'] = None

        super(Key, __self__).__init__(
            'aws:kms/key:Key',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

