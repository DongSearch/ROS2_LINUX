# Interface
Interface defines messages. using this Interface, it makes it much easier to reuse and share the parameter between nodes

# Make
it is similar to make package

'''
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

#after build, check if it is rightly done

ros2 interface show interface name/srv/..

  
'''
