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


class ContainerSpec(object):

    def __init__(self, name, image, systemDisk, command=None, args=None, env=None, secret=None, tty=None, workingDir=None, livenessProbe=None, readinessProbe=None, resources=None, volumeMounts=None):
        """
        :param name:  容器名称
        :param command: (Optional) 容器执行命令，如果不指定默认是docker镜像的ENTRYPOINT。总长度256个字符。
        :param args: (Optional) 容器执行命令的参数，如果不指定默认是docker镜像的CMD。总长度2048个字符。
        :param env: (Optional) 容器执行的环境变量；如果和镜像中的环境变量Key相同，会覆盖镜像中的值。长度范围：[0-100]
        :param image:  镜像名称 </br>
容器镜像名字。 nginx:latest。长度范围：[1-500]
1. Docker Hub官方镜像通过类似nginx, mysql/mysql-server的名字指定 </br> 
2. repository长度最大256个字符，tag最大128个字符，registry最大255个字符 </br> 

        :param secret: (Optional) 镜像仓库secret名字。如果目前不传，默认选择dockerHub镜像
        :param tty: (Optional) 容器是否分配tty。默认不分配
        :param workingDir: (Optional) 容器的工作目录。如果不指定，默认是根目录（/）；必须是绝对路径；长度范围：[0-1024]
        :param livenessProbe: (Optional) 容器存活探针配置
        :param readinessProbe: (Optional) 容器服务就绪探针配置
        :param resources: (Optional) 容器计算资源配置
        :param systemDisk:  容器计算资源配置
        :param volumeMounts: (Optional) 容器计算资源配置
        """

        self.name = name
        self.command = command
        self.args = args
        self.env = env
        self.image = image
        self.secret = secret
        self.tty = tty
        self.workingDir = workingDir
        self.livenessProbe = livenessProbe
        self.readinessProbe = readinessProbe
        self.resources = resources
        self.systemDisk = systemDisk
        self.volumeMounts = volumeMounts
