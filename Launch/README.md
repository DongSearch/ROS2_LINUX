# rclpy
it is a client library to help user create node and manage them easily with Python, which was orginally done with C++ before

- it consist of Node, Publisher & Subscriber, Service, Action, Parameter, Executor
- ROS structure : user code - **rcl** - rmw - rmw adapter - middleware(QoS and messsage storage)


# Launch
ROS 2 requires running many commands in different terminals, which can be cumbersome. Launch files help by collecting all the nodes and packages we need into a single executable. Using configuration files (YAML) also makes it easier to change parameters.

- process

```
#1. make 'lunch folder' in package where we want to make lunch file

#2. write ros2 launch.py

#3. edit setup file adding path of share folder that would be created after build

#4. build and source

#5. with ros2 command, it allows to execute program
ros2 run pkg node

```
