from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic_turtle1',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
                
            ]
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2_turtle2',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle2/cmd_vel'),
                
            ]
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name ='mimic_turtle3',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle3/cmd_vel')
            ]
        )


    ])