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


class CreateRoleInfo(object):

    def __init__(self, roleName, type, assumeRolePolicyDocument, path=None, description=None, maxSessionDuration=None):
        """
        :param path: (Optional) 角色路径
        :param roleName:  角色名：支持4-64位的字母，数字以及-和_, 以字母开头
        :param type:  角色类型，3-服务角色，4-用户角色
        :param assumeRolePolicyDocument:  角色信任关系策略
        :param description: (Optional) 描述，0~256个字符
        :param maxSessionDuration: (Optional) 最大会话时长3600~43200秒，默认3600秒
        """

        self.path = path
        self.roleName = roleName
        self.type = type
        self.assumeRolePolicyDocument = assumeRolePolicyDocument
        self.description = description
        self.maxSessionDuration = maxSessionDuration
