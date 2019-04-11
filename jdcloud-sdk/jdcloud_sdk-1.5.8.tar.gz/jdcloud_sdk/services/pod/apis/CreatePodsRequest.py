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


class CreatePodsRequest(JDCloudRequest):
    """
    - 创建pod需要通过实名认证
- hostname规范
    - 支持两种方式：以标签方式书写或以完整主机名方式书写
    - 标签规范
        - 0-9，a-z(不分大小写)和-（减号），其他的都是无效的字符串
        - 不能以减号开始，也不能以减号结尾
        - 最小1个字符，最大63个字符
    - 完整的主机名由一系列标签与点连接组成
        - 标签与标签之间使用“.”(点)进行连接
        - 不能以“.”(点)开始，也不能以“.”(点)结尾
        - 整个主机名（包括标签以及分隔点“.”）最多有63个ASCII字符
    - 正则：`^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9])(.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]))*$`
- 网络配置
    - 指定主网卡配置信息
        - 必须指定subnetId
        - 可以指定elasticIp规格来约束创建的弹性IP，带宽取值范围[1-100]Mbps，步进1Mbps
        - 可以指定网卡的主IP(primaryIpAddress)和辅助IP(secondaryIpAddresses)，此时maxCount只能为1
        - 可以设置网卡的自动删除autoDelete属性，指明是否删除实例时自动删除网卡
        - 安全组securityGroup需与子网Subnet在同一个私有网络VPC内
        - 一个 pod 创建时必须指定一个安全组，至多指定5个安全组
        - 主网卡deviceIndex设置为1
- 存储
    - volume分为root volume和data volume，root volume的挂载目录是/，data volume的挂载目录可以随意指定
    - volume的底层存储介质当前只支持cloud类别，也就是云硬盘
    - root volume
        - root volume只能是cloud类别
        - 云硬盘类型可以选择ssd、premium-hdd
        - 磁盘大小
            - ssd：范围[10,100]GB，步长为10G
            - premium-hdd：范围[10,100]GB，步长为10G
        - 自动删除
            - 默认自动删除
        - 可以选择已存在的云硬盘
    - data volume
        - data volume当前只能选择cloud类别
        - 云硬盘类型可以选择ssd、premium-hdd
        - 磁盘大小
            - ssd：范围[20,1000]GB，步长为10G
            - premium-hdd：范围[20,3000]GB，步长为10G
        - 自动删除
            - 默认自动删除
        - 可以选择已存在的云硬盘
        - 可以从快照创建磁盘
- pod 容器日志
    - default：默认在本地分配10MB的存储空间，自动rotate
- 其他
    - 创建完成后，pod 状态为running
    - maxCount为最大努力，不保证一定能达到maxCount

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreatePodsRequest, self).__init__(
            '/regions/{regionId}/pods', 'POST', header, version)
        self.parameters = parameters


class CreatePodsParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.podSpec = None
        self.maxCount = None

    def setPodSpec(self, podSpec):
        """
        :param podSpec: (Optional) pod 创建参数
        """
        self.podSpec = podSpec

    def setMaxCount(self, maxCount):
        """
        :param maxCount: (Optional) 购买实例数量；取值范围：[1,100]
        """
        self.maxCount = maxCount

