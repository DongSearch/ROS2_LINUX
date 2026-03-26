from launch import LaunchDescription
from launch_ros.actions import Node
import os
import xacro
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # urdf_file = os.path.join(
    #     os.getcwd(),
    #     "src/my_human_description/urdf/human.urdf"
    # )
    pkg_path = get_package_share_directory('my_human_description')
    xacro_file = os.path.join(pkg_path,'urdf','human.urdf.xacro')
    doc = xacro.process_file(xacro_file)
    robot_desc = doc.toxml()

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description" : robot_desc}]
        ),

        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui"
        ),
        Node(
            package="rviz2",
            executable="rviz2"
        )
    ])