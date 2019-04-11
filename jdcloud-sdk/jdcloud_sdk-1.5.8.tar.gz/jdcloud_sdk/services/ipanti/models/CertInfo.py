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


class CertInfo(object):

    def __init__(self, domain=None, from=None, to=None, user=None, sigAlgName=None, issuer=None):
        """
        :param domain: (Optional) 通用名称
        :param from: (Optional) 证书生效时间
        :param to: (Optional) 证书到期时间
        :param user: (Optional) 证书组织
        :param sigAlgName: (Optional) 加密算法
        :param issuer: (Optional) 颁发者
        """

        self.domain = domain
        self.from = from
        self.to = to
        self.user = user
        self.sigAlgName = sigAlgName
        self.issuer = issuer
