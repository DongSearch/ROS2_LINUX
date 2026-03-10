# Package
A package is the most basic unit in ROS2.
It contains nodes, libraries, configuration files, launch files, dependencies, and other resources needed to run ROS2 programs.


## programming rule
- Files & packages : lower_snake_case(only lowercase and _ to separate words) eg. my_node.py
- Messages / Services / Actions (interface files) : CamelCase(each word starts with uppercase) eg. SpawnTurtle.srv


## Underlay and Overlay
Underlay : 
- Base ROS2 installation
- Includes core libraries, tools, messages, and environment setup
- Activated using

Overlay : 
- User workspace built on top of underlay
- Used to develop and install custom packages
- Activated using


## Domain
ROS_DOMAIN_ID
- Used to separate different ROS2 networks.

ROS_LOCALHOST_ONLY
- Restricts communication to the same computer only. and prevents communication over the network.

## Package elements
Node
- Executable program that performs a specific task.

Launch file
- Starts multiple nodes with parameters.

Configuration file
- YAML file defining parameters.

Library
- Reusable functions or classes.

Resource
- Data files (meshes, maps, images, etc.)

Test
- Unit or integration tests.

Documentation
- Explanation of package usage.

## Package files
- package.xml : it contains metadata that defines dependencies, and it is used by the build system to determine dependency order

- setup.py & setup.cfg : setup.py is used for python packages and defines installation information and executable ntry points, while setup.cfg is used for configuration file for build and installation settings
- CMakeLists.txt : it describe how to build code in package that specify compiler, library, source file


## How to create package
```
#first step : make workspace and src
mkdir -p workspace/src

#second step : move to **src** and create package
cd workspace/src
ros2 pkg create --build-type ament_python test1_pkg

#third step : python coding(make node, do message).... and add it to setup.py(entry_points)!
 
#forth step : move to workspace(**no src**) and do colcon to build
colcon build --symlink-install

#fifth step : source
source ./install/setup.bash

#last step :execute file
ros2 run test1_pkg nodename
```


## Data Type
| Message Type        | Package         | Data Structure             | Description         | Example Usage             |
| ------------------- | --------------- | -------------------------- | ------------------- | ------------------------- |
| `String`            | `std_msgs`      | `string data`              | text message        | log, simple communication |
| `Bool`              | `std_msgs`      | `bool data`                | true / false        | state flag                |
| `Int32`             | `std_msgs`      | `int32 data`               | integer value       | counter                   |
| `Float32`           | `std_msgs`      | `float32 data`             | floating value      | sensor data               |
| `Int32MultiArray`   | `std_msgs`      | `int32[] data`             | integer array       | multiple values           |
| `Float32MultiArray` | `std_msgs`      | `float32[] data`           | float array         | vector / sensor set       |
| `Vector3`           | `geometry_msgs` | `x, y, z`                  | 3D vector           | velocity, acceleration    |
| `Point`             | `geometry_msgs` | `x, y, z`                  | coordinate point    | target position           |
| `Twist`             | `geometry_msgs` | `linear + angular`         | robot velocity      | robot movement            |
| `Pose`              | `geometry_msgs` | `position + orientation`   | robot pose          | localization              |
| `PoseStamped`       | `geometry_msgs` | `pose + header(time)`      | timestamped pose    | navigation                |
| `Image`             | `sensor_msgs`   | image data                 | camera frame        | vision                    |
| `LaserScan`         | `sensor_msgs`   | lidar scan array           | lidar sensor data   | obstacle detection        |
| `Imu`               | `sensor_msgs`   | orientation + accel + gyro | IMU data            | robot orientation         |
| `PointCloud2`       | `sensor_msgs`   | 3D point cloud             | depth / lidar       | mapping                   |
| `Odometry`          | `nav_msgs`      | pose + velocity            | robot movement info | localization              |
| `Path`              | `nav_msgs`      | array of poses             | planned path        | navigation                |

