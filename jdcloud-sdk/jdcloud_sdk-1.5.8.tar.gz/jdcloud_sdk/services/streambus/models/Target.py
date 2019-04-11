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


class Target(object):

    def __init__(self, name=None, recordSize=None, cycle=None):
        """
        :param name: (Optional) 需要归档的目的地
        :param recordSize: (Optional) 当达到这个数据量时开始归档
        :param cycle: (Optional) 进行归档任务的时间周期
        """

        self.name = name
        self.recordSize = recordSize
        self.cycle = cycle
