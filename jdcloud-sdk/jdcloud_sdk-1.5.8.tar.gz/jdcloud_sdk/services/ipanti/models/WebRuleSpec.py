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


class WebRuleSpec(object):

    def __init__(self, domain, protocol, originType, algorithm, webSocketStatus, port=None, httpsPort=None, originAddr=None, onlineAddr=None, originDomain=None, forceJump=None, customPortStatus=None, httpOrigin=None, httpsCertContent=None, httpsRsaKey=None, certId=None):
        """
        :param domain:  子域名
        :param protocol:  协议: http, https 至少一个为 true
        :param port: (Optional) HTTP协议的端口号, 如80, 81; 如果 protocol.http 为 true, 至少配置一个端口, 最多添加 5 个
        :param httpsPort: (Optional) HTTPS协议的端口号，如443, 8443; 如果 protocol.https 为 true, 至少配置一个端口, 最多添加 5 个
        :param originType:  回源类型：A或者CNAME
        :param originAddr: (Optional) originType 为 A 时，需要设置该字段
        :param onlineAddr: (Optional) 备用的回源地址列表，可以配置为一个域名或者多个 ip 地址
        :param originDomain: (Optional) 回源域名,originType为CNAME时需要指定该字段
        :param algorithm:  转发规则：wrr->带权重的轮询，rr->不带权重的轮询
        :param forceJump: (Optional) 是否开启 https 强制跳转，当 protocol 为 HTTP_HTTPS 时可以配置该属性
  - 0 不开启强制跳转
  - 1 开启强制跳转

        :param customPortStatus: (Optional) 是否为自定义端口号，0为默认 1为自定义
        :param httpOrigin: (Optional) 是否开启http回源, 当勾选HTTPS时可以配置该属性
  - 0 不开启
  - 1 开启

        :param webSocketStatus:  是否开启 WebSocket, 0 为不开启, 1 为开启
        :param httpsCertContent: (Optional) 证书内容
        :param httpsRsaKey: (Optional) 证书私钥
        :param certId: (Optional) 证书 Id
  - 如果传 certId, 请确认已经上传了相应的证书
  - certId 缺省时网站规则将使用 httpsCertContent, httpsRsaKey 对应的证书
        """

        self.domain = domain
        self.protocol = protocol
        self.port = port
        self.httpsPort = httpsPort
        self.originType = originType
        self.originAddr = originAddr
        self.onlineAddr = onlineAddr
        self.originDomain = originDomain
        self.algorithm = algorithm
        self.forceJump = forceJump
        self.customPortStatus = customPortStatus
        self.httpOrigin = httpOrigin
        self.webSocketStatus = webSocketStatus
        self.httpsCertContent = httpsCertContent
        self.httpsRsaKey = httpsRsaKey
        self.certId = certId
