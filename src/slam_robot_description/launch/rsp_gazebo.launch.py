import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('slam_robot_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'slam_robot.urdf')
    world_file = os.path.join(pkg_share, 'worlds', 'slam_room.world')
    rviz_config_file = os.path.join(pkg_share, 'config', 'slam.rviz')

    with open(urdf_file, 'r') as infp:
        robot_description_config = infp.read()

    params = {'robot_description': robot_description_config, 'use_sim_time': True}

    # Robot State Publisher Node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    # Launch Gazebo Sim
    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ]),
        launch_arguments={'gz_args': f'-r {world_file}'}.items()
    )

    # Spawn Robot Entity
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-string', robot_description_config, '-name', 'slam_robot', '-z', '0.1'],
        output='screen'
    )

    # Bridge ROS 2 <-> Gazebo topics
    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
            '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image',
            '/camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo'
        ],
        output='screen'
    )

    # RViz2 Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        node_robot_state_publisher,
        gazebo_sim,
        spawn_entity,
        ros_gz_bridge,
        rviz_node
    ])