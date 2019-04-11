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


class DeleteFileSystemRequest(JDCloudRequest):
    """
    -   删除一个文件系统，一旦删除，该文件系统将不存在，也无法访问已删除的文件系统里的任何内容。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteFileSystemRequest, self).__init__(
            '/regions/{regionId}/fileSystems/{fileSystemId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteFileSystemParameters(object):

    def __init__(self, regionId, fileSystemId, ):
        """
        :param regionId: 地域ID
        :param fileSystemId: 文件系统ID
        """

        self.regionId = regionId
        self.fileSystemId = fileSystemId

