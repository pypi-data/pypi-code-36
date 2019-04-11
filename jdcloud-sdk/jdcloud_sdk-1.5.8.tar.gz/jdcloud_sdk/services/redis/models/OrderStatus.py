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


class OrderStatus(object):

    def __init__(self, total=None, success=None, fail=None, inProcess=None, resourceIds=None):
        """
        :param total: (Optional) 订单总数
        :param success: (Optional) 成功数
        :param fail: (Optional) 失败数
        :param inProcess: (Optional) 正在处理数
        :param resourceIds: (Optional) 成功的资源Id
        """

        self.total = total
        self.success = success
        self.fail = fail
        self.inProcess = inProcess
        self.resourceIds = resourceIds
