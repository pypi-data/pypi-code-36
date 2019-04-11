# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    allow_version_upgrade: pulumi.Output[bool]
    """
    If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true
    """
    automated_snapshot_retention_period: pulumi.Output[float]
    """
    The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.
    """
    availability_zone: pulumi.Output[str]
    """
    The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.
    """
    cluster_identifier: pulumi.Output[str]
    """
    The Cluster Identifier. Must be a lower case
    string.
    """
    cluster_parameter_group_name: pulumi.Output[str]
    """
    The name of the parameter group to be associated with this cluster.
    """
    cluster_public_key: pulumi.Output[str]
    """
    The public key for the cluster
    """
    cluster_revision_number: pulumi.Output[str]
    """
    The specific revision number of the database in the cluster
    """
    cluster_security_groups: pulumi.Output[list]
    """
    A list of security groups to be associated with this cluster.
    """
    cluster_subnet_group_name: pulumi.Output[str]
    """
    The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
    """
    cluster_type: pulumi.Output[str]
    """
    The cluster type to use. Either `single-node` or `multi-node`.
    """
    cluster_version: pulumi.Output[str]
    """
    The version of the Amazon Redshift engine software that you want to deploy on the cluster.
    The version selected runs on all the nodes in the cluster.
    """
    database_name: pulumi.Output[str]
    """
    The name of the first database to be created when the cluster is created.
    If you do not provide a name, Amazon Redshift will create a default database called `dev`.
    """
    dns_name: pulumi.Output[str]
    """
    The DNS name of the cluster
    """
    elastic_ip: pulumi.Output[str]
    """
    The Elastic IP (EIP) address for the cluster.
    """
    encrypted: pulumi.Output[bool]
    """
    If true , the data in the cluster is encrypted at rest.
    """
    endpoint: pulumi.Output[str]
    """
    The connection endpoint
    """
    enhanced_vpc_routing: pulumi.Output[bool]
    """
    If true , enhanced VPC routing is enabled.
    """
    final_snapshot_identifier: pulumi.Output[str]
    """
    The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, `skip_final_snapshot` must be false.
    """
    iam_roles: pulumi.Output[list]
    """
    A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.
    """
    kms_key_id: pulumi.Output[str]
    """
    The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be set to true.
    """
    logging: pulumi.Output[dict]
    """
    Logging, documented below.
    """
    master_password: pulumi.Output[str]
    """
    Password for the master DB user.
    Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
    contain at least one uppercase letter, one lowercase letter, and one number.
    """
    master_username: pulumi.Output[str]
    """
    Username for the master DB user.
    """
    node_type: pulumi.Output[str]
    """
    The node type to be provisioned for the cluster.
    """
    number_of_nodes: pulumi.Output[float]
    """
    The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.
    """
    owner_account: pulumi.Output[str]
    """
    The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
    """
    port: pulumi.Output[float]
    """
    The port number on which the cluster accepts incoming connections.
    The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.
    """
    preferred_maintenance_window: pulumi.Output[str]
    """
    The weekly time range (in UTC) during which automated cluster maintenance can occur.
    Format: ddd:hh24:mi-ddd:hh24:mi
    """
    publicly_accessible: pulumi.Output[bool]
    """
    If true, the cluster can be accessed from a public network. Default is `true`.
    """
    skip_final_snapshot: pulumi.Output[bool]
    """
    Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.
    """
    snapshot_cluster_identifier: pulumi.Output[str]
    """
    The name of the cluster the source snapshot was created from.
    """
    snapshot_copy: pulumi.Output[dict]
    """
    Configuration of automatic copy of snapshots from one region to another. Documented below.
    """
    snapshot_identifier: pulumi.Output[str]
    """
    The name of the snapshot from which to create the new cluster.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vpc_security_group_ids: pulumi.Output[list]
    """
    A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
    """
    def __init__(__self__, resource_name, opts=None, allow_version_upgrade=None, automated_snapshot_retention_period=None, availability_zone=None, cluster_identifier=None, cluster_parameter_group_name=None, cluster_public_key=None, cluster_revision_number=None, cluster_security_groups=None, cluster_subnet_group_name=None, cluster_type=None, cluster_version=None, database_name=None, elastic_ip=None, encrypted=None, endpoint=None, enhanced_vpc_routing=None, final_snapshot_identifier=None, iam_roles=None, kms_key_id=None, logging=None, master_password=None, master_username=None, node_type=None, number_of_nodes=None, owner_account=None, port=None, preferred_maintenance_window=None, publicly_accessible=None, skip_final_snapshot=None, snapshot_cluster_identifier=None, snapshot_copy=None, snapshot_identifier=None, tags=None, vpc_security_group_ids=None, __name__=None, __opts__=None):
        """
        Provides a Redshift Cluster Resource.
        
        > **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_version_upgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true
        :param pulumi.Input[float] automated_snapshot_retention_period: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.
        :param pulumi.Input[str] availability_zone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.
        :param pulumi.Input[str] cluster_identifier: The Cluster Identifier. Must be a lower case
               string.
        :param pulumi.Input[str] cluster_parameter_group_name: The name of the parameter group to be associated with this cluster.
        :param pulumi.Input[str] cluster_public_key: The public key for the cluster
        :param pulumi.Input[str] cluster_revision_number: The specific revision number of the database in the cluster
        :param pulumi.Input[list] cluster_security_groups: A list of security groups to be associated with this cluster.
        :param pulumi.Input[str] cluster_subnet_group_name: The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
        :param pulumi.Input[str] cluster_type: The cluster type to use. Either `single-node` or `multi-node`.
        :param pulumi.Input[str] cluster_version: The version of the Amazon Redshift engine software that you want to deploy on the cluster.
               The version selected runs on all the nodes in the cluster.
        :param pulumi.Input[str] database_name: The name of the first database to be created when the cluster is created.
               If you do not provide a name, Amazon Redshift will create a default database called `dev`.
        :param pulumi.Input[str] elastic_ip: The Elastic IP (EIP) address for the cluster.
        :param pulumi.Input[bool] encrypted: If true , the data in the cluster is encrypted at rest.
        :param pulumi.Input[str] endpoint: The connection endpoint
        :param pulumi.Input[bool] enhanced_vpc_routing: If true , enhanced VPC routing is enabled.
        :param pulumi.Input[str] final_snapshot_identifier: The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, `skip_final_snapshot` must be false.
        :param pulumi.Input[list] iam_roles: A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.
        :param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key. When specifying `kms_key_id`, `encrypted` needs to be set to true.
        :param pulumi.Input[dict] logging: Logging, documented below.
        :param pulumi.Input[str] master_password: Password for the master DB user.
               Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and
               contain at least one uppercase letter, one lowercase letter, and one number.
        :param pulumi.Input[str] master_username: Username for the master DB user.
        :param pulumi.Input[str] node_type: The node type to be provisioned for the cluster.
        :param pulumi.Input[float] number_of_nodes: The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.
        :param pulumi.Input[str] owner_account: The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
        :param pulumi.Input[float] port: The port number on which the cluster accepts incoming connections.
               The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range (in UTC) during which automated cluster maintenance can occur.
               Format: ddd:hh24:mi-ddd:hh24:mi
        :param pulumi.Input[bool] publicly_accessible: If true, the cluster can be accessed from a public network. Default is `true`.
        :param pulumi.Input[bool] skip_final_snapshot: Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.
        :param pulumi.Input[str] snapshot_cluster_identifier: The name of the cluster the source snapshot was created from.
        :param pulumi.Input[dict] snapshot_copy: Configuration of automatic copy of snapshots from one region to another. Documented below.
        :param pulumi.Input[str] snapshot_identifier: The name of the snapshot from which to create the new cluster.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[list] vpc_security_group_ids: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
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

        __props__['allow_version_upgrade'] = allow_version_upgrade

        __props__['automated_snapshot_retention_period'] = automated_snapshot_retention_period

        __props__['availability_zone'] = availability_zone

        if cluster_identifier is None:
            raise TypeError('Missing required property cluster_identifier')
        __props__['cluster_identifier'] = cluster_identifier

        __props__['cluster_parameter_group_name'] = cluster_parameter_group_name

        __props__['cluster_public_key'] = cluster_public_key

        __props__['cluster_revision_number'] = cluster_revision_number

        __props__['cluster_security_groups'] = cluster_security_groups

        __props__['cluster_subnet_group_name'] = cluster_subnet_group_name

        __props__['cluster_type'] = cluster_type

        __props__['cluster_version'] = cluster_version

        __props__['database_name'] = database_name

        __props__['elastic_ip'] = elastic_ip

        __props__['encrypted'] = encrypted

        __props__['endpoint'] = endpoint

        __props__['enhanced_vpc_routing'] = enhanced_vpc_routing

        __props__['final_snapshot_identifier'] = final_snapshot_identifier

        __props__['iam_roles'] = iam_roles

        __props__['kms_key_id'] = kms_key_id

        __props__['logging'] = logging

        __props__['master_password'] = master_password

        __props__['master_username'] = master_username

        if node_type is None:
            raise TypeError('Missing required property node_type')
        __props__['node_type'] = node_type

        __props__['number_of_nodes'] = number_of_nodes

        __props__['owner_account'] = owner_account

        __props__['port'] = port

        __props__['preferred_maintenance_window'] = preferred_maintenance_window

        __props__['publicly_accessible'] = publicly_accessible

        __props__['skip_final_snapshot'] = skip_final_snapshot

        __props__['snapshot_cluster_identifier'] = snapshot_cluster_identifier

        __props__['snapshot_copy'] = snapshot_copy

        __props__['snapshot_identifier'] = snapshot_identifier

        __props__['tags'] = tags

        __props__['vpc_security_group_ids'] = vpc_security_group_ids

        __props__['dns_name'] = None

        super(Cluster, __self__).__init__(
            'aws:redshift/cluster:Cluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

