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


class DeleteCustomLiveStreamWatermarkTemplateRequest(JDCloudRequest):
    """
    删除用户自定义水印模板
- 删除用户自定义水印模板之前必须先删除此模板在各域名、应用、流级别的水印设置

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteCustomLiveStreamWatermarkTemplateRequest, self).__init__(
            '/watermarkCustoms/{template}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteCustomLiveStreamWatermarkTemplateParameters(object):

    def __init__(self, template, ):
        """
        :param template: 水印模板

        """

        self.template = template

