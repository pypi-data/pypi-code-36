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


class DescribeMetricDataRequest(JDCloudRequest):
    """
    查看某资源多个监控项数据，metric介绍1：<a href="https://docs.jdcloud.com/cn/monitoring/metrics">Metrics</a>
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeMetricDataRequest, self).__init__(
            '/regions/{regionId}/metrics/{metric}/metricData', 'GET', header, version)
        self.parameters = parameters


class DescribeMetricDataParameters(object):

    def __init__(self, regionId, metric, serviceCode, resourceId):
        """
        :param regionId: 地域 Id
        :param metric: 监控项英文标识(id)
        :param serviceCode: 资源的类型，取值vm, lb, ip, database 等
        :param resourceId: 资源的uuid
        """

        self.regionId = regionId
        self.metric = metric
        self.aggrType = None
        self.downSampleType = None
        self.startTime = None
        self.endTime = None
        self.timeInterval = None
        self.tags = None
        self.groupBy = None
        self.rate = None
        self.serviceCode = serviceCode
        self.resourceId = resourceId

    def setAggrType(self, aggrType):
        """
        :param aggrType: (Optional) 聚合方式，默认等于downSampleType或avg，可选值参考:sum、avg、last、min、max
        """
        self.aggrType = aggrType

    def setDownSampleType(self, downSampleType):
        """
        :param downSampleType: (Optional) 采样方式，默认等于aggrType或avg，可选值参考：sum、avg、last、min、max
        """
        self.downSampleType = downSampleType

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询时间范围的开始时间， UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询时间范围的结束时间， UTC时间，格式：2016-12- yyyy-MM-dd'T'HH:mm:ssZ（为空时，将由startTime与timeInterval计算得出）
        """
        self.endTime = endTime

    def setTimeInterval(self, timeInterval):
        """
        :param timeInterval: (Optional) 时间间隔：1h，6h，12h，1d，3d，7d，14d，固定时间间隔，timeInterval默认为1h，当前时间往 前1h
        """
        self.timeInterval = timeInterval

    def setTags(self, tags):
        """
        :param tags: (Optional) 自定义标签/tag；至少要传一个tag，且tag.Values不为空
        """
        self.tags = tags

    def setGroupBy(self, groupBy):
        """
        :param groupBy: (Optional) 是否对查询的tags分组
        """
        self.groupBy = groupBy

    def setRate(self, rate):
        """
        :param rate: (Optional) 是否求速率
        """
        self.rate = rate

