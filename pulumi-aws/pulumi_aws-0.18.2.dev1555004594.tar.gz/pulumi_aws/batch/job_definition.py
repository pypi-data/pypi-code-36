# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class JobDefinition(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name of the job definition.
    """
    container_properties: pulumi.Output[str]
    """
    A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
    provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the job definition.
    """
    parameters: pulumi.Output[dict]
    """
    Specifies the parameter substitution placeholders to set in the job definition.
    """
    retry_strategy: pulumi.Output[dict]
    """
    Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
    Maximum number of `retry_strategy` is `1`.  Defined below.
    """
    revision: pulumi.Output[float]
    """
    The revision of the job definition.
    """
    timeout: pulumi.Output[dict]
    """
    Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
    """
    type: pulumi.Output[str]
    """
    The type of job definition.  Must be `container`
    """
    def __init__(__self__, resource_name, opts=None, container_properties=None, name=None, parameters=None, retry_strategy=None, timeout=None, type=None, __name__=None, __opts__=None):
        """
        Provides a Batch Job Definition resource.
        
        ## retry_strategy
        
        `retry_strategy` supports the following:
        
        * `attempts` - (Optional) The number of times to move a job to the `RUNNABLE` status. You may specify between `1` and `10` attempts.
        
        ## timeout
        
        `timeout` supports the following:
        
        * `attempt_duration_seconds` - (Optional) The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is `60` seconds.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_properties: A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
               provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
        :param pulumi.Input[str] name: Specifies the name of the job definition.
        :param pulumi.Input[dict] parameters: Specifies the parameter substitution placeholders to set in the job definition.
        :param pulumi.Input[dict] retry_strategy: Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
               Maximum number of `retry_strategy` is `1`.  Defined below.
        :param pulumi.Input[dict] timeout: Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
        :param pulumi.Input[str] type: The type of job definition.  Must be `container`
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

        __props__['container_properties'] = container_properties

        __props__['name'] = name

        __props__['parameters'] = parameters

        __props__['retry_strategy'] = retry_strategy

        __props__['timeout'] = timeout

        if type is None:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        __props__['arn'] = None
        __props__['revision'] = None

        super(JobDefinition, __self__).__init__(
            'aws:batch/jobDefinition:JobDefinition',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

