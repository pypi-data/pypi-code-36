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


class DownloadCCAttackLogsRequest(JDCloudRequest):
    """
    下载 CC 攻击日志
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DownloadCCAttackLogsRequest, self).__init__(
            '/regions/{regionId}/attacklog:CC/download', 'GET', header, version)
        self.parameters = parameters


class DownloadCCAttackLogsParameters(object):

    def __init__(self, regionId, startTime, endTime, ):
        """
        :param regionId: 区域 Id
        :param startTime: 开始时间, 只能下载最近 60 天以内的数据, UTC 时间, 格式：yyyy-MM-dd'T'HH:mm:ssZ
        :param endTime: 查询的结束时间, UTC 时间, 格式：yyyy-MM-dd'T'HH:mm:ssZ
        """

        self.regionId = regionId
        self.startTime = startTime
        self.endTime = endTime
        self.instanceId = None

    def setInstanceId(self, instanceId):
        """
        :param instanceId: (Optional) 高防实例 ID
        """
        self.instanceId = instanceId

