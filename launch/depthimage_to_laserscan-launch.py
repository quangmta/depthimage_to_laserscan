# Copyright 2019 Open Source Robotics Foundation, Inc.
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

# /* Author: Gary Liu */

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    param_config = os.path.join(get_package_share_directory('depthimage_to_laserscan'), 'cfg', 'param.yaml')
    return LaunchDescription([
        Node(
            package='depthimage_to_laserscan',
            executable='depthimage_to_laserscan_node',
            name='depthimage_to_laserscan_node',
            remappings=[#('depth','/estimated_depth'),
                        ('depth','/processed_depth_image'),
                        # ('depth','/camera/aligned_depth_to_color/image_raw'),
                        ('depth_camera_info', '/camera/color/camera_info')],
            parameters=[param_config])
    ])
