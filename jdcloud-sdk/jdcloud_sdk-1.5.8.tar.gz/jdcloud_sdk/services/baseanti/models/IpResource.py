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


class IpResource(object):

    def __init__(self, ip=None, bandwidth=None, safeStatus=None):
        """
        :param ip: (Optional) 公网IP
        :param bandwidth: (Optional) 带宽上限，单位Mbps
        :param safeStatus: (Optional) 0->安全 1->清洗 2->黑洞
        """

        self.ip = ip
        self.bandwidth = bandwidth
        self.safeStatus = safeStatus
