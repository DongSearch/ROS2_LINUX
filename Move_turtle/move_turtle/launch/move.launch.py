from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():

    turtlesim = Node(
        package='turtlesim',
        executable='turtlesim_node'
    )

    server = Node(
        package='move_turtle',
        executable='act'
    )

    client = TimerAction(
        period=2.0,
        actions =[
            Node(
                package='move_turtle',
                executable='cli'
            )
        ]
    )

    return LaunchDescription([
        turtlesim,
        server,
        client
    ])