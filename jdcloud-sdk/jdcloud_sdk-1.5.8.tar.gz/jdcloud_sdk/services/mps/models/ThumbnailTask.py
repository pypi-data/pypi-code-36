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


class ThumbnailTask(object):

    def __init__(self, source, target, taskID=None, status=None, errorCode=None, createdTime=None, lastUpdatedTime=None, rule=None):
        """
        :param taskID: (Optional) 任务ID (readonly)
        :param status: (Optional) 状态 (SUCCESS, ERROR, PENDDING, RUNNING) (readonly)
        :param errorCode: (Optional) 错误码 (readonly)
        :param createdTime: (Optional) 任务创建时间 时间格式(GMT): yyyy-MM-dd’T’HH:mm:ss.SSS’Z’  (readonly)
        :param lastUpdatedTime: (Optional) 任务创建时间 时间格式(GMT): yyyy-MM-dd’T’HH:mm:ss.SSS’Z’  (readonly)
        :param source:  
        :param target:  
        :param rule: (Optional) 
        """

        self.taskID = taskID
        self.status = status
        self.errorCode = errorCode
        self.createdTime = createdTime
        self.lastUpdatedTime = lastUpdatedTime
        self.source = source
        self.target = target
        self.rule = rule
