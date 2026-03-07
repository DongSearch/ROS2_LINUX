## Conditon and Installation(humble)
- Ubuntu 22.04 LTS(Humble)
- check to Ubuntu version
```
 lsb_release -a
# Ubuntu 22.04.4 LTS
```

- How to install ROS2
```
cd ~/path

#git install
sudo apt update
sudo apt install git

#permission
chmod +x ros2-humble-desktop-main.sh

#installation
./ros2-humble-desktop-main.sh
```

- check to installation
```
chmod +x ./tutorial.sh
./tutorial.sh

#if installation is done well,

Finished <<< launch_testing_examples
Summary: 22 packages finished

```

```
#verify
ros2 run examples_rclcpp_minimal_publisher publisher_member_function
#check version
printenv ROS_DISTRO

```

- to use ROS2 command, the environment should be set up first. but to avoid long coding every time, we add it to bash file

```
gedit ~/.bashrc
# add
source /opt/ros/humble/setup.bash
```
