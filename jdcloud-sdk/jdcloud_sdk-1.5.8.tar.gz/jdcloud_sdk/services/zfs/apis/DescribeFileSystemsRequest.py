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


class DescribeFileSystemsRequest(JDCloudRequest):
    """
    -   查询文件系统列表。
-   filters多个过滤条件之间是逻辑与(AND)，每个条件内部的多个取值是逻辑或(OR)

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeFileSystemsRequest, self).__init__(
            '/regions/{regionId}/fileSystems', 'GET', header, version)
        self.parameters = parameters


class DescribeFileSystemsParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞)
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) fileSystemId - 文件系统ID，精确匹配，支持多个
name - 文件系统名称，模糊匹配，支持单个
status - 文件系统状态，精确匹配，支持多个 FileSystem Status/creating、available、in-use

        """
        self.filters = filters

