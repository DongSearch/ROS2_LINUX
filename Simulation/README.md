# SLAM (Simultaneous Localization and Mapping)
Localization: Estimating and continuously tracking the robot’s current position and orientation within an environment.
Mapping: Building a map of the surrounding environment using sensor data.

## Loop Closure

As a robot moves, small errors from sensors and odometry accumulate over time (drift).
When the robot returns to a previously visited location, it may fail to recognize it, causing the accumulated error to grow significantly.

- Loop closure solves this problem by:

- Detecting that the robot has revisited the same place
- Comparing features (e.g., landmarks, scan data)
- If similarity is high, aligning the current map with the past map
- Correcting accumulated errors in the trajectory and map

# Principles

There are two main approaches to mapping:

## 1. LiDAR-based SLAM

Uses LiDAR sensors to measure distances and generate maps from point cloud data.

Advantages:

Accurate distance measurement
Less sensitive to lighting conditions

Disadvantages:

Sensitive to noise (e.g., reflective surfaces, environmental interference)

Types:

2D LiDAR: Measures distance and angle (x, y plane)
3D LiDAR: Measures distance, angle, and height (x, y, z)

Examples of LiDAR SLAM:

GMapping:
Mainly used in ROS1
Sensitive to sensor noise and odometry errors
Cartographer:
Supports ROS1 & ROS2
Works with both 2D and 3D LiDAR
More robust and provides accurate localization


## 2. Visual SLAM (Camera-based)

Uses cameras to extract visual features and estimate motion.

Advantages:

Rich environmental information (texture, color)
Lower cost compared to LiDAR

Disadvantages:

Sensitive to lighting changes
Requires more computation

## Odometry

Odometry estimates the robot’s motion based on:

Wheel encoders
IMU (Inertial Measurement Unit)

It provides short-term motion estimation but accumulates error over time.

## SLAM Workflow
Sensor Initialization
Angle parameters: angular resolution, field of view (FOV), vertical angle
Time parameters: scan rate, timestamp, time of flight
Range parameters: minimum/maximum range, accuracy, noise
Data Collection
Gather sensor data (LiDAR, camera, IMU)
Feature Extraction
Extract meaningful features (edges, corners, keypoints)
State Estimation
Estimate robot pose using sensor fusion
Map Optimization
Apply loop closure and optimization to reduce accumulated errors

## Navigation

After generating a map using SLAM, the robot navigates to a target location.

Key Components:
Path Planning
Finds an optimal path from the current position to the goal
Behavior Tree
Manages decision-making and robot behaviors
Trajectory Tracking
Ensures the robot follows the planned path accurately
## Notes
Simulation environments can be computationally expensive
It is important to keep each module efficient while maintaining realism

## Terminology
World: The global reference frame or environment
Model: A complete robot or object representation
Link: A rigid body within a model
Joint: Connects links and defines motion
Sensor: Device that collects environmental data
Plugin: Software component that extends functionality (e.g., in Gazebo or ROS2)
