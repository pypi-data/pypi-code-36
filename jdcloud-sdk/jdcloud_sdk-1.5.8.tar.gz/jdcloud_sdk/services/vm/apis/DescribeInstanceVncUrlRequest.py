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


class DescribeInstanceVncUrlRequest(JDCloudRequest):
    """
    获取云主机vnc，用于连接管理云主机。<br>
vnc地址的有效期为1个小时，调用接口获取vnc地址后如果1个小时内没有使用，vnc地址自动失效，再次使用需要重新获取。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstanceVncUrlRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/vnc', 'GET', header, version)
        self.parameters = parameters


class DescribeInstanceVncUrlParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID
        :param instanceId: 云主机ID
        """

        self.regionId = regionId
        self.instanceId = instanceId

