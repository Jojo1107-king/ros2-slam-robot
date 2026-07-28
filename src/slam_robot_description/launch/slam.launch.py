import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('slam_robot_description')
    
    # Path to SLAM config and RViz config
    slam_params_file = os.path.join(pkg_share, 'config', 'mapper_params_online_async.yaml')
    rviz_config_file = os.path.join(pkg_share, 'config', 'slam.rviz')

    # SLAM Toolbox Launch Node
    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py')
        ]),
        launch_arguments={
            'use_sim_time': 'true',
            'slam_params_file': slam_params_file
        }.items()
    )

    # RViz Node with auto-loaded config file
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        slam_toolbox,
        #rviz_node
    ])