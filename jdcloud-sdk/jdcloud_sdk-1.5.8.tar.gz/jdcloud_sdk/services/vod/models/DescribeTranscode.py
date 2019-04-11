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


class DescribeTranscode(object):

    def __init__(self, coderateId=None, name=None, format=None, width=None, height=None, videoCodec=None, videoCoderate=None, videoFramerate=None, audioId=None, audioCodec=None, audioCoderate=None, sampleRate=None, channel=None, updateTime=None, createTime=None):
        """
        :param coderateId: (Optional) 模板ID
        :param name: (Optional) 模板名称
        :param format: (Optional) 封装格式
        :param width: (Optional) 宽
        :param height: (Optional) 高
        :param videoCodec: (Optional) 视频编码
        :param videoCoderate: (Optional) 视频码率
        :param videoFramerate: (Optional) 视频帧率
        :param audioId: (Optional) 音频ID
        :param audioCodec: (Optional) 音频编码
        :param audioCoderate: (Optional) 音频码率
        :param sampleRate: (Optional) 音频采样率
        :param channel: (Optional) 音频声道数
        :param updateTime: (Optional) 修改时间
        :param createTime: (Optional) 创建时间
        """

        self.coderateId = coderateId
        self.name = name
        self.format = format
        self.width = width
        self.height = height
        self.videoCodec = videoCodec
        self.videoCoderate = videoCoderate
        self.videoFramerate = videoFramerate
        self.audioId = audioId
        self.audioCodec = audioCodec
        self.audioCoderate = audioCoderate
        self.sampleRate = sampleRate
        self.channel = channel
        self.updateTime = updateTime
        self.createTime = createTime
