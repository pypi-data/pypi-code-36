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


class DescribeAlarmHistoryAllRegionRequest(JDCloudRequest):
    """
    查询报警历史
检索条件组合优先级从高到低为
1. alarmId
2. serviceCode
2.1 serviceCode + resourceId
2.2 serviceCode + resourceIds
3. serviceCodes
4. 用户所有规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAlarmHistoryAllRegionRequest, self).__init__(
            '/ruleNoticeHistory', 'POST', header, version)
        self.parameters = parameters


class DescribeAlarmHistoryAllRegionParameters(object):

    def __init__(self, ):
        """
        """

        self.pageNumber = None
        self.pageSize = None
        self.serviceCode = None
        self.resourceId = None
        self.resourceIdList = None
        self.alarmId = None
        self.alarming = None
        self.serviceCodeList = None
        self.startTime = None
        self.endTime = None
        self.ruleType = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
        """
        self.pageSize = pageSize

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 产品线
        """
        self.serviceCode = serviceCode

    def setResourceId(self, resourceId):
        """
        :param resourceId: (Optional) 资源Id
        """
        self.resourceId = resourceId

    def setResourceIdList(self, resourceIdList):
        """
        :param resourceIdList: (Optional) resourceId列表
        """
        self.resourceIdList = resourceIdList

    def setAlarmId(self, alarmId):
        """
        :param alarmId: (Optional) 规则Id
        """
        self.alarmId = alarmId

    def setAlarming(self, alarming):
        """
        :param alarming: (Optional) 正在报警, 取值为1
        """
        self.alarming = alarming

    def setServiceCodeList(self, serviceCodeList):
        """
        :param serviceCodeList: (Optional) 产品线列表
        """
        self.serviceCodeList = serviceCodeList

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 开始时间
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间
        """
        self.endTime = endTime

    def setRuleType(self, ruleType):
        """
        :param ruleType: (Optional) 规则类型,默认查询1， 1表示资源监控，6表示站点监控,7表示可用性监控
        """
        self.ruleType = ruleType

    def setFilters(self, filters):
        """
        :param filters: (Optional) 服务码或资源Id列表
filter name 为serviceCodes表示查询多个产品线的规则
filter name 为resourceIds表示查询多个资源的规则
        """
        self.filters = filters

