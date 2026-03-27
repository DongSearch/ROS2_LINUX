# SLAM(Simultaneous Localization and Mapping)
Localizaiton : track current position of robot
Mapping : generate map around the robot

## Loop Closure
robot accumulate error by keeping moving, and it will come back to the point where it starts move, but if they can't recognize it, the error get explode.
-> so loop closure connect the past map and current map by fixing the error( analysing similarity between feature points, and if it has high similarity, they estimate it as same point)


## Principal
there are two way to map
1. Lidar(Visaul) : using lidar they get distance data, and then it generates map using point cloud data
they can measure exact distance, and less sensitive to weather, but it weaks noise(light)
- 2D : measure distance ,angle
- 3D : distance, angle, altitude

  type of Lidar slam
  GMapping : ROS1, sensitive to sensro, odmetry error
  Cartographer : ROS1 & ROS2, 2D&3D, robust to error, more exact localizaiton estimation

odometry : 

## Workflow
- sensor initialization :
1. angle parameters : angular resolution, FOV, vertical angle
2. time parameters: scam rate, timestap,time of flight
3. range parameters: range, accuracy,noise

- data collection

- feature extraction

# Navigation
after getting map from SLAM, it plan the route to reach target point

path planning : 
behavior tree : 
trajectory tracking : 




# NOTICE
- simulation takes up a lot of resources, so it is important to make function of each part as simple as possible but looks real


# Terminology
- World
- model
- link
- joint
- sensor
- plugin
