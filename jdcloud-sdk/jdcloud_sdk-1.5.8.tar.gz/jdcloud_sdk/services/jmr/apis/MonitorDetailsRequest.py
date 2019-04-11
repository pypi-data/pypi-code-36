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


class MonitorDetailsRequest(JDCloudRequest):
    """
    服务存活状态监控明细数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(MonitorDetailsRequest, self).__init__(
            '/regions/{regionId}/monitorDetails', 'POST', header, version)
        self.parameters = parameters


class MonitorDetailsParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.clusterId = None
        self.service = None

    def setClusterId(self, clusterId):
        """
        :param clusterId: (Optional) 集群ID
        """
        self.clusterId = clusterId

    def setService(self, service):
        """
        :param service: (Optional) 服务名称，如HADOOP
        """
        self.service = service

