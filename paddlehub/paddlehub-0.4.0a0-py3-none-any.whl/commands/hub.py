# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from paddlehub.common.logger import logger
from paddlehub.commands.base_command import BaseCommand
from paddlehub.commands import show
from paddlehub.commands import help
from paddlehub.commands import version
from paddlehub.commands import run
from paddlehub.commands import download


class HubCommand(BaseCommand):
    name = "hub"

    def __init__(self, name):
        super(HubCommand, self).__init__(name)
        self.show_in_help = False

    def exec(self, argv):
        logger.setLevel("NOLOG")

        if not argv:
            help.command.exec(argv)
            exit(1)
            return False
        sub_command = argv[0]
        if not sub_command in BaseCommand.command_dict:
            print("ERROR: unknown command '%s'" % sub_command)
            help.command.exec(argv)
            exit(1)
            return False

        command = BaseCommand.command_dict[sub_command]
        return command.exec(argv[1:])


command = HubCommand.instance()


def main():
    command.exec(sys.argv[1:])


if __name__ == "__main__":
    command.exec(sys.argv[1:])
