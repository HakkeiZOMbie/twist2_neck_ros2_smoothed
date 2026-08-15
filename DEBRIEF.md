This file is a guide for developers. If you are a user, read the README file instead.

Note: A working prototype has been create, thus making this note irrelevant. Consult the README instead

# TWIST2 Neck Ros2
This repository is a ROS2 package for enabling XR teleoperation of the TWIST2 Neck (teleoperation with a VR headset).
The package should contain:
- `neck_node`, a ROS2 node for controlling the TWIST2 Neck
- `twist2_neck_launch`, a launch file for bringing up the neck node and necessary nodes
   for streaming camera input to the headset

Details are given below.

# `neck_node`
This node should read the head tf published by `isaac_ros_teleop`'s `teleop_ros2_node`
and actuate the neck using `TWIST2-Neck-Controller`.
The links to the repositories may be found here
- IsaacTeleop: [repo](https://github.com/NVIDIA/IsaacTeleop) [docs](https://nvidia.github.io/IsaacTeleop/main/index.html)
- `isaac_ros_teleop`: [repo](https://github.com/TWIST2-C1/isaac_ros_teleop) [docs](https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_teleop/isaac_ros_teleop/index.html) (the docs may be outdated, check code to be sure!)
- Neck Controller: [repo](https://github.com/TWIST2-C1/TWIST2-Neck-Controller)
- ROS2: [docs](https://docs.ros.org/en/jazzy/index.html)

# Camera streaming
The TWIST2 Neck contains two Tear Four C1 Cameras, which when connected to a machine running linux, shows up as
two `v4l2` cameras. The feeds from this two camera should be streamed back to the headset. 
This will be done using [camera_viz](https://nvidia.github.io/IsaacTeleop/main/references/camera_streaming.html).
Currently, `camera_viz` does not have an implementation for stereo vision using two v4l2 cameras, but this
capability can be extended by creating a class that inherits `FrameSource` 

Note: `/dev/video0` is left, `/dev/video2` is right

# Launch file
Learn more about them [here](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Creating-Launch-Files.html).
Python launchfiles are preferred