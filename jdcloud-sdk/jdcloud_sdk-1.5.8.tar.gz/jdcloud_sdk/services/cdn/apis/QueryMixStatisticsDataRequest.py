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


class QueryMixStatisticsDataRequest(JDCloudRequest):
    """
    查询统计数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryMixStatisticsDataRequest, self).__init__(
            '/statistics', 'POST', header, version)
        self.parameters = parameters


class QueryMixStatisticsDataParameters(object):

    def __init__(self, ):
        """
        """

        self.startTime = None
        self.endTime = None
        self.domain = None
        self.fields = None
        self.area = None
        self.isp = None
        self.period = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.endTime = endTime

    def setDomain(self, domain):
        """
        :param domain: (Optional) 需要查询的域名, 必须为用户pin下有权限的域名
        """
        self.domain = domain

    def setFields(self, fields):
        """
        :param fields: (Optional) 需要查询的字段
        """
        self.fields = fields

    def setArea(self, area):
        """
        :param area: (Optional) 
        """
        self.area = area

    def setIsp(self, isp):
        """
        :param isp: (Optional) 
        """
        self.isp = isp

    def setPeriod(self, period):
        """
        :param period: (Optional) 时间粒度，可选值:[oneMin,fiveMin,followTime],followTime只会返回一个汇总后的数据
        """
        self.period = period

