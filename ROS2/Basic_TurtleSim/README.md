# Play with Turtlesim

## Spawn 2 turtles and move independently

- first terminal(spawn first turtle)
```
ros2 run turtlesim turtlesim_node
```
- second terminal(spawn second turtle)
```
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name: 'turtle2}"
```

- third terminal(move foirstturtle)
```
ros2 run pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z:2.0}}"
```

- forth terminal(move second turtle)
```
ros2 run pub /turtle2/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -2.0}, angular: {z:3.0}}"
```
<img width="504" height="530" alt="image" src="https://github.com/user-attachments/assets/c3ca6a78-981b-4cde-80e4-9c7327102c91" />

-rqt_graph

In the graph, we can see that there are 5 nodes in total. However, only 3 nodes are mainly involved in the communication:
two ros2cli nodes and the turtlesim node.

We spawn a turtle using a service (/spawn).Since the service is called only once, it does not appear in the graph.
The service server is provided by the turtlesim node.

The two ros2cli nodes are used to move the turtles.
They publish velocity commands to the topics:

/turtle1/cmd_vel
/turtle2/cmd_vel

The turtlesim node subscribes to these topics to control the turtles.

<img width="834" height="367" alt="image" src="https://github.com/user-attachments/assets/70436313-a08e-4683-80f0-669d6ce2f333" />
