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


class SetProtocolConvertRequest(JDCloudRequest):
    """
    设置转协议
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetProtocolConvertRequest, self).__init__(
            '/liveDomain/{domain}/protocolConvert', 'POST', header, version)
        self.parameters = parameters


class SetProtocolConvertParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.certificate = None
        self.rsaKey = None
        self.protocolConverts = None

    def setCertificate(self, certificate):
        """
        :param certificate: (Optional) https证书,转https格式时必传
        """
        self.certificate = certificate

    def setRsaKey(self, rsaKey):
        """
        :param rsaKey: (Optional) https私钥，转https格式时必传
        """
        self.rsaKey = rsaKey

    def setProtocolConverts(self, protocolConverts):
        """
        :param protocolConverts: (Optional) 
        """
        self.protocolConverts = protocolConverts

