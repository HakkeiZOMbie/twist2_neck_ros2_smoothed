from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
    """Launch the twist2 neck demo stack"""
    isaac_ros_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('isaac_ros_teleop'),
                'launch',
                'isaac_ros_teleop.launch.py'
            )
        )
    )
    neck_config_arg = DeclareLaunchArgument(
        name='neck_config',
        default_value=os.path.join(
            get_package_share_directory('twist2_neck_ros2'),
            'config.json'
        ),
        description='Neck controller config filepath'
    )

    neck_node = Node(
        package='twist2_neck_ros2',
        executable='neck_node',
        name='neck_node',
        output='screen',
        arguments=[
            '--config',
            LaunchConfiguration('neck_config')
        ]
    )

    camera_config_arg = DeclareLaunchArgument(
        name='camera_config',
        default_value=os.path.join(
            get_package_share_directory('twist2_neck_ros2'),
            'camera_config.yaml'
        ),
        description='Camera (camera_viz) config filepath'
    )

    camera_viz = ExecuteProcess(
        cmd=[
            'bash',
            '-c',
            'source "$(conda info --base)/etc/profile.d/conda.sh" && '
            'conda activate camera_env && '
            'exec python "$@"',
            'bash',
            os.path.join(
                get_package_share_directory('isaac_teleop_core'),
                'camera_viz',
                'camera_viz.py',
            ),
            LaunchConfiguration('camera_config'),
        ],
        output='screen',
    )

    return LaunchDescription([
        neck_config_arg,
        camera_config_arg,
        isaac_ros_launch,
        neck_node,
        TimerAction(
            period=5.0,
            actions=[
                camera_viz,
            ]
        )
    ])
