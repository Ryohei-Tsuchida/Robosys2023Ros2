# SPDX-FileCopyrightText:2023 Ryohei Tsuchida
# SPDX-License-Identifier:BSD-3-Clau

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    prime_ans = launch_ros.actions.Node(
        package='mypkg',
        executable='prime_ans',
        output='screen'
    )

    randam_number = launch_ros.actions.Node(
        package='mypkg',
        executable='randam_number',
        output='screen'
    )
    return launch.LaunchDescription([prime_ans, randam_number])

