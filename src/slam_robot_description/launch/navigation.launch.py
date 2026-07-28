import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_share = get_package_share_directory('slam_robot_description')
    
    map_yaml_file = os.path.join(pkg_share, 'maps', 'my_map.yaml')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_yaml_file,
            'use_sim_time': 'true',
            'autostart': 'true',
            'use_composition': 'True'
        }.items()
    )

    return LaunchDescription([
        nav2_launch
    ])