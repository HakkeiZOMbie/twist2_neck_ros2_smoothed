# Twist2 Neck Demo ROS2 Package
This is a ROS2 package for enabling teleoperation with [RLG's custom Twist2 Neck](https://cad.onshape.com/documents/47fa8d1ecda3a73fd33251d4/w/729f53ea65e8681e728c0bdd/e/0594b845c8982d02745d40e1) with NVIDIA's [IsaacTeleop](https://nvidia.github.io/IsaacTeleop/main/index.html). 

The package includes
- `neck_node`, a node for reading the head tf published by `isaac_ros_teleop` and
  commanding the neck's servo motors
- `twist2_neck.launch.py`, a launch file for bringing up the entire teleoperation stack

## Setting up your enviroment
Unfortunately, because this package depends on IsaacTeleop, it is only compatible on
machines with CUDA (although `neck_node` itself does not depend on it). The development and
testing for this package has been done with the Jetson Thor in mind, so you may need to
modify these setup instructions for your system.

### ROS2
Follow the instructions for the [installation of ROS2 Jazzy](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

### IsaacTeleop
This package utilizes a new pre-release version of IsaacTeleop. Follow the [guide](https://nvidia.github.io/IsaacTeleop/main/getting_started/quick_start.html)
and install it, making sure that the 1.5.x version is installed, but be sure to install to system rather than to a venv (use `sudo` and `--system --break-system-packages`)

### ROS2 workspace
Create a new workspace in your preferred directory. Under `src/`, clone this repository and our fork
of `isaac_ros_teleop`
```bash
git clone --recursive https://github.com/TWIST2-C1/isaac_ros_teleop.git
```
```bash
git clone --recursive https://github.com/TWIST2-C1/twist2_neck_ros2.git
```

### camera_viz python environment
The modified Twist2 Neck utilizes two TIER IV C1 cameras and camera streaming is done through a
[fork](https://github.com/TWIST2-C1/IsaacTeleop) of [`camera_viz`](https://nvidia.github.io/IsaacTeleop/main/references/camera_streaming.html).
The C1 cameras are recognized as generic `v4l2` cameras and are combined into a single stereo source.
`camera_viz` needs its own python virtual environment in order to work, and you may set one up as follows:
note: **DO NOT USE SYSTEM PYTHON FOR THIS!!** `camera_viz` uses numpy v2 and will break compatibility.
1. Open a terminal in the workspace directory
2. Create a new conda venv named `camera_venv`
   ```bash
   conda create --name camera_venv python=3.12
   ```
3. Run `camera_viz`'s setup script (for jetson)
   ```bash
   ./src/isaac_ros_teleop/isaac_teleop_core/IsaacTeleop/examples/camera_viz/camera_viz.sh setup --venv "$CONDA_PREFIX" --jetson --no-oakd 
   ```

### `isaac_ros_teleop` setup
You will need to create a symbolic link for `teleop_ros2_interfaces`. From the workspace directory, run
```bash
ln -s ./src/isaac_ros_teleop/isaac_teleop_core/IsaacTeleop/examples/teleop_ros2/teleop_ros2_interfaces ./src/
```

Finally, after all is said and done, try running `colcon build --symlink-install`! 

## Running the stack
Source the workspace's enviroment
```bash
source install/setup.sh
```
and run the launch file
```bash
ros2 launch twist2_neck_ros2 twist2_neck.launch.py
```

To do:
- Update `isaac_ros_teleop`'s .gitmodules to point at correct IsaacTeleop commit