# Software License Agreement (BSD License)
#
# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Base ROS python library for manipulating ROS packages and stacks.
"""

from .common import MANIFEST_FILE, ResourceNotFound, STACK_FILE
from .environment import get_etc_ros_dir, get_log_dir, get_ros_home, \
    get_ros_package_path, get_ros_paths, get_ros_root, \
    get_test_results_dir, on_ros_path
from .manifest import InvalidManifest, Manifest, parse_manifest_file
from .rospack import expand_to_packages, get_package_name, \
    get_stack_version_by_dir, list_by_path, RosPack, RosStack

# same version as in:
# - setup.py
# - stdeb.cfg
__version__ = '1.1.8'

__all__ = (
    'MANIFEST_FILE', 'ResourceNotFound', 'STACK_FILE',
    'get_etc_ros_dir', 'get_log_dir', 'get_ros_home',
    'get_ros_package_path', 'get_ros_paths', 'get_ros_root',
    'get_test_results_dir', 'on_ros_path',
    'InvalidManifest', 'Manifest', 'parse_manifest_file',
    'get_package_name', 'RosPack', 'RosStack',
    'list_by_path', 'expand_to_packages', 'get_stack_version_by_dir',
)
