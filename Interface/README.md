# Interface

- An **Interface** defines `.msg`, `.srv`, or `.action` files in ROS2.
- It standardizes data exchange between nodes and makes it easier to reuse and share parameters.

## Create

Even for Python projects, interfaces must be created with `ament_cmake`

```
#src(eventhough we will do with python, we should put cmake here for interface)
ros2 pkg create --build-type ament_cmake interface_name

#move to interface
mdkir srv msg action

#make service,toic,atcion depending on what we need(extention should be same like .srv, .msg, .action

#define input,output

float32 a
int64 b

---
float32 result


#add dependencies to package.xml
  <buildtool_depend>ament_cmake</buildtool_depend>
  <build_depend>rosidl_default_generators</build_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>

#add it to CMakeList.txt as well

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
"srv/Cal.srv")

#after then, same as package
colcon build --package-select name
source install/setup.bash

#Check that request and response fields display correctly.

ros2 interface show interface name/srv/..
```
!!!! don't forget to add dependencies to normal package we use!!!!

## ROS2 package.xml Key Tags for Interface Packages

| Tag | Location | Description | Example | Notes / Usage in Interface Packages |
|-----|---------|------------|--------|-----------------------------------|
| `<buildtool_depend>` | Required | Specifies the build tool needed to build the package | `<buildtool_depend>ament_cmake</buildtool_depend>` | Always required; for interface packages, typically `ament_cmake` |
| `<build_depend>` | Required | Packages needed at build time | `<build_depend>rosidl_default_generators</build_depend>` | Required for generating `.srv`, `.msg`, `.action` files |
| `<exec_depend>` | Required | Packages needed at runtime | `<exec_depend>rosidl_default_runtime</exec_depend>` | Needed for nodes that use the generated messages/services |
| `<depend>` | Optional / Recommended | General dependency used for build and/or runtime | `<depend>rclpy</depend>` | Useful if Python nodes will use this interface |
| `<member_of_group>` | Required for interface packages | Marks the package as an interface package, ensuring correct build order | `<member_of_group>rosidl_interface_packages</member_of_group>` | Essential for `.srv`, `.msg`, `.action` packages |
| `<test_depend>` | Optional | Packages needed for testing or linting | `<test_depend>ament_lint_auto</test_depend>` | Useful to include ROS2 recommended test packages |
| `<maintainer>` | Required | Name and email of the package maintainer | `<maintainer email="you@example.com">Your Name</maintainer>` | Standard ROS2 requirement |
| `<license>` | Required | License declaration for the package | `<license>Apache-2.0</license>` | Standard ROS2 requirement |
| `<export>` | Optional | Extra build or package information | `<export><build_type>ament_cmake</build_type></export>` | For interface packages, usually specifies build type as `ament_cmake` |

## Notes on Interface Packages

- **buildtool_depend**: Always `ament_cmake` for interface packages. Python nodes using the interface don’t affect this.
- **build_depend**: Must include `rosidl_default_generators` to generate code for messages, services, and actions.
- **exec_depend**: Must include `rosidl_default_runtime` for runtime support of generated code.
- **member_of_group**: Essential. Without this, the build system may not build the interface package before dependent node packages.
- **depend / exec_depend for Python nodes**: If Python nodes will use this interface, add `rclpy` or other required dependencies as `<depend>` or `<exec_depend>`.
- **Testing**: Optional but recommended to include `ament_lint_auto`, `ament_lint_common`, etc. for code quality checks.
- **Export / build_type**: Must match how the package is built (`ament_cmake` for interface packages, `ament_python` for Python node packages).
