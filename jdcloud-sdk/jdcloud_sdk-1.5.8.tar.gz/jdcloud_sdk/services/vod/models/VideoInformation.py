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


class VideoInformation(object):

    def __init__(self, mid=None, videoName=None, url=None, imgUrl=None, categoryId=None, category=None, status=None, size=None, duration=None, tags=None, notes=None, coderateId=None, logoId=None, md5=None, clientIp=None, clientId=None, createTime=None, updateTime=None, imgList=None):
        """
        :param mid: (Optional) 视频ID
        :param videoName: (Optional) 视频名称
        :param url: (Optional) 片源地址
        :param imgUrl: (Optional) 封面图地址
        :param categoryId: (Optional) 视频分类ID
        :param category: (Optional) 视频分类名称
        :param status: (Optional) 状态
        :param size: (Optional) 文件大小
        :param duration: (Optional) 视频时长
        :param tags: (Optional) 标签
        :param notes: (Optional) 视频介绍
        :param coderateId: (Optional) 转码模板ID
        :param logoId: (Optional) 水印模板ID
        :param md5: (Optional) MD5值
        :param clientIp: (Optional) 上传客户
        :param clientId: (Optional) 上传业务ID
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param imgList: (Optional) 截图成品
        """

        self.mid = mid
        self.videoName = videoName
        self.url = url
        self.imgUrl = imgUrl
        self.categoryId = categoryId
        self.category = category
        self.status = status
        self.size = size
        self.duration = duration
        self.tags = tags
        self.notes = notes
        self.coderateId = coderateId
        self.logoId = logoId
        self.md5 = md5
        self.clientIp = clientIp
        self.clientId = clientId
        self.createTime = createTime
        self.updateTime = updateTime
        self.imgList = imgList
