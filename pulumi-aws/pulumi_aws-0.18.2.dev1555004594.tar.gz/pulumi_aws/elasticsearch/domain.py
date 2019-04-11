# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Domain(pulumi.CustomResource):
    access_policies: pulumi.Output[str]
    """
    IAM policy document specifying the access policies for the domain
    """
    advanced_options: pulumi.Output[dict]
    """
    Key-value string pairs to specify advanced configuration options.
    Note that the values for these configuration options must be strings (wrapped in quotes) or they
    may be wrong and cause a perpetual diff, causing Terraform to want to recreate your Elasticsearch
    domain on every apply.
    """
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the domain.
    """
    cluster_config: pulumi.Output[dict]
    """
    Cluster configuration of the domain, see below.
    """
    cognito_options: pulumi.Output[dict]
    domain_id: pulumi.Output[str]
    """
    Unique identifier for the domain.
    """
    domain_name: pulumi.Output[str]
    """
    Name of the domain.
    """
    ebs_options: pulumi.Output[dict]
    """
    EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
    """
    elasticsearch_version: pulumi.Output[str]
    """
    The version of Elasticsearch to deploy. Defaults to `1.5`
    """
    encrypt_at_rest: pulumi.Output[dict]
    """
    Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
    """
    endpoint: pulumi.Output[str]
    """
    Domain-specific endpoint used to submit index, search, and data upload requests.
    """
    kibana_endpoint: pulumi.Output[str]
    """
    Domain-specific endpoint for kibana without https scheme.
    * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
    * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
    """
    log_publishing_options: pulumi.Output[list]
    """
    Options for publishing slow logs to CloudWatch Logs.
    """
    node_to_node_encryption: pulumi.Output[dict]
    """
    Node-to-node encryption options. See below.
    """
    snapshot_options: pulumi.Output[dict]
    """
    Snapshot related options, see below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource
    """
    vpc_options: pulumi.Output[dict]
    """
    VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
    """
    def __init__(__self__, resource_name, opts=None, access_policies=None, advanced_options=None, cluster_config=None, cognito_options=None, domain_name=None, ebs_options=None, elasticsearch_version=None, encrypt_at_rest=None, log_publishing_options=None, node_to_node_encryption=None, snapshot_options=None, tags=None, vpc_options=None, __name__=None, __opts__=None):
        """
        Manages an AWS Elasticsearch Domain.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[dict] advanced_options: Key-value string pairs to specify advanced configuration options.
               Note that the values for these configuration options must be strings (wrapped in quotes) or they
               may be wrong and cause a perpetual diff, causing Terraform to want to recreate your Elasticsearch
               domain on every apply.
        :param pulumi.Input[dict] cluster_config: Cluster configuration of the domain, see below.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input[dict] ebs_options: EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        :param pulumi.Input[str] elasticsearch_version: The version of Elasticsearch to deploy. Defaults to `1.5`
        :param pulumi.Input[dict] encrypt_at_rest: Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        :param pulumi.Input[list] log_publishing_options: Options for publishing slow logs to CloudWatch Logs.
        :param pulumi.Input[dict] node_to_node_encryption: Node-to-node encryption options. See below.
        :param pulumi.Input[dict] snapshot_options: Snapshot related options, see below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource
        :param pulumi.Input[dict] vpc_options: VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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

        __props__['access_policies'] = access_policies

        __props__['advanced_options'] = advanced_options

        __props__['cluster_config'] = cluster_config

        __props__['cognito_options'] = cognito_options

        __props__['domain_name'] = domain_name

        __props__['ebs_options'] = ebs_options

        __props__['elasticsearch_version'] = elasticsearch_version

        __props__['encrypt_at_rest'] = encrypt_at_rest

        __props__['log_publishing_options'] = log_publishing_options

        __props__['node_to_node_encryption'] = node_to_node_encryption

        __props__['snapshot_options'] = snapshot_options

        __props__['tags'] = tags

        __props__['vpc_options'] = vpc_options

        __props__['arn'] = None
        __props__['domain_id'] = None
        __props__['endpoint'] = None
        __props__['kibana_endpoint'] = None

        super(Domain, __self__).__init__(
            'aws:elasticsearch/domain:Domain',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

