# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateAuditRequest(JDCloudRequest):
    """
    开启SQL Server的数据库审计功能，目前支持实例级的数据库审计。用户可以根据需要开启、关闭审计、自定义审计策略，并下载审计文件。审计文件为原生的SQL Server审计文件，缺省保存6个月。<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateAuditRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/audit', 'POST', header, version)
        self.parameters = parameters


class CreateAuditParameters(object):

    def __init__(self, regionId, instanceId, enabled):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param enabled: 要开启的审计选项，各个选项之间用英文逗号或空格进行分割，例如：DATABASE_OBJECT_ACCESS_GROUP,ACKUP_RESTORE_GROU等<br>各个数据库版本支持的审计选项可以通过接口[getAuditOptions](./getAuditOptions.md)获得，各个审计项的具体含义可以参看微软的官方文档
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.enabled = enabled

