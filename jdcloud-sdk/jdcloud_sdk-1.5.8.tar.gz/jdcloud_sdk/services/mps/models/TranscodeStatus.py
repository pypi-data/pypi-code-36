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


class TranscodeStatus(object):

    def __init__(self, status, errorCode=None, notifyMessage=None):
        """
        :param status:  状态 (SUCESS, ERROR, PENDDING, RUNNING)
        :param errorCode: (Optional) 错误码
        :param notifyMessage: (Optional) 通知消息, 由work调用, 暂时方案
        """

        self.status = status
        self.errorCode = errorCode
        self.notifyMessage = notifyMessage
