# TF2
TF2 is a ROS2 library that manages coordinate frame transformations between different parts of a robot.
why is it so important?   
- track robot pose in space
- relate sensor data to robot body
- enable motion planning and control
- visualization

## Command

1. TransformSTamped
   - Represents a transform between two coordinate frames
```
header.frame_id → parent frame
child_frame_id → child frame
transform.translation → position (x, y, z)
transform.rotation → orientation (quaternion)
```
2. TRansformBroadcaster
   - broadcasts transforms to the tf2 system.
```
self.br = TransformBroadcaster(self)
self.br.sendTransform(transform_msg)
```

# URDF(Unified Robot Description Format)

URDF is an XML-based format used to describe the structure of a robot

URDF files can become very long and repetitive.
Xacro allows you to define reusable templates (macros).


## Components

📌 1. Link (Rigid Body)

Represents a physical part of the robot.

<link name="torso">
  <visual>
    <geometry>
      <box size="0.3 0.2 0.5"/>
    </geometry>
  </visual>
</link>

        
📌 2. Joint (Connection Between Links)

Defines how two links are connected.

<joint name="shoulder" type="revolute">
  <parent link="torso"/>
  <child link="arm"/>
  <origin xyz="0 0.2 0.2"/>
  <axis xyz="0 0 1"/>
</joint>


* Joint types
- fixed : no movement
- revolute : rotational joint
- prismatic : linear sliding joint

📌 3. Visual, Collision, Inertial    
🔹 Visual    

Defines how the robot looks in visualization tools.

<visual>
  <geometry>
    <box size="0.3 0.2 0.5"/>
  </geometry>
</visual>
🔹 Collision

Defines the shape used for collision detection (usually simplified).

<collision>
  <geometry>
    <box size="0.3 0.2 0.5"/>
  </geometry>
</collision>
🔹 Inertial

Defines physical properties required for simulation.

<inertial>
  <mass value="1.0"/>
  <inertia ixx="0.1" iyy="0.1" izz="0.1"
           ixy="0.0" ixz="0.0" iyz="0.0"/>
</inertial>

# Becareful!!!!
1. when you publish topic to move robot, make sure to remove joint_state_publisher(it conflicts message)
2. msg.header.stamp = self.get_clock().now().to_msg(), that should be included to move robot in rviz


# workflow
1. create package (with ament_cmake)
2. make rviz, urdf launch folder
3. design robot shape using making urdf.xacro files
4. add install rule
```
install(
  DIRECTORY launch urdf
  DESTINATION share/${PROJECT_NAME}
)
```
5. make lunchfile
```
robot_state_publisher
joint_state_publisher
rviz2
```

# Make Human robot walking x coordinate


[Screencast from 2026년 03월 26일 21시 07분 36초.webm](https://github.com/user-attachments/assets/575f161f-5558-411a-9944-32f95bb03908)

