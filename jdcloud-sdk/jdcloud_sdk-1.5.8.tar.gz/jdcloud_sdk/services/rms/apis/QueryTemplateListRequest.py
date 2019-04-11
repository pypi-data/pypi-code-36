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


class QueryTemplateListRequest(JDCloudRequest):
    """
    查询富媒体短信内容列表接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryTemplateListRequest, self).__init__(
            '/regions/{regionId}/queryTemplateList', 'POST', header, version)
        self.parameters = parameters


class QueryTemplateListParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.appId = None
        self.searchKey = None
        self.pageNum = None
        self.pageLimit = None
        self.status = None
        self.title = None
        self.startTime = None
        self.endTime = None

    def setAppId(self, appId):
        """
        :param appId: (Optional) appId参数
        """
        self.appId = appId

    def setSearchKey(self, searchKey):
        """
        :param searchKey: (Optional) searchKey参数
        """
        self.searchKey = searchKey

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) pageNum参数
        """
        self.pageNum = pageNum

    def setPageLimit(self, pageLimit):
        """
        :param pageLimit: (Optional) pageLimit参数
        """
        self.pageLimit = pageLimit

    def setStatus(self, status):
        """
        :param status: (Optional) status参数
        """
        self.status = status

    def setTitle(self, title):
        """
        :param title: (Optional) title参数
        """
        self.title = title

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) startTime参数
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) endTime参数
        """
        self.endTime = endTime

