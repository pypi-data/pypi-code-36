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


class RebootInstanceRequest(JDCloudRequest):
    """
    重启单个云主机，只能重启<b>running</b>状态的云主机，云主机没有正在进行中的任务才可重启。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RebootInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:rebootInstance', 'POST', header, version)
        self.parameters = parameters


class RebootInstanceParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID
        :param instanceId: 云主机ID
        """

        self.regionId = regionId
        self.instanceId = instanceId

