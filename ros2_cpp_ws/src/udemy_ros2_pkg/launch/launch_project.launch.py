from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Path to joy config
    joy_config_path = PathJoinSubstitution(
        [FindPackageShare("udemy_ros2_pkg"), "config", "joy.yaml"]
    )
    
    return LaunchDescription([
        # Node(
        #     package="udemy_ros2_pkg",
        #     executable="rpm_pub",
        #     name="rpm_pub_node",
        #     parameters=[
        #         {"rpm_val": 5.0}
        #     ]
        # ),
        # Node(
        #     package="udemy_ros2_pkg",
        #     executable="speed_calc",
        #     name="speed_calc_node",
        #     parameters=[
        #         {"wheel_radius": 10/100} # Centimeters to meters
        #     ]
        # ),
        # Joy node (PS4 controller)
        Node(
            package="joy",
            executable="joy_node",
            name="joy_node",
            output=["screen"]
        ),
        # Teleop node for converting PS4 input to cmd_vel
        Node(
            package="teleop_twist_joy",
            executable="teleop_node",
            name="teleop_twist_joy_node",
            output=["screen"],
            parameters=[joy_config_path]
        ),

        ExecuteProcess(
            cmd=['ros2', 'topic', 'echo', '/speed'],
            output='screen'
        )

    ])