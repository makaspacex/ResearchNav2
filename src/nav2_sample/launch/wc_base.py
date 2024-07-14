import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    package_name = 'nav2_sample'
    urdf_name = "wheelchair_base.urdf"
    pkg_share = FindPackageShare(package=package_name).find(package_name)
    urdf_model_path = os.path.join(pkg_share, f'urdf/{urdf_name}')
    urdf_model_path = "/home/makafly/Desktop/ResearchNav2/src/nav2_sample/urdf/wheelchair_base.urdf"
    
    parameters=[{
        'robot_description': ParameterValue(
            Command(['xacro ', str(urdf_model_path)]), value_type=str
        )
    }]
    
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=parameters
        )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=parameters
        )
    
    ld = LaunchDescription()
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_node)

    return ld
