import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    randam_ans = launch_ros.actions.Node(
        package='mypkg',
        executable='randam_ans',
        output='screen'
    )

    randam_number = launch_ros.actions.Node(
        package='mypkg',
        executable='randam_number',
        output='screen'
    )
    return launch.LaunchDescription([randam_ans, randam_number])

