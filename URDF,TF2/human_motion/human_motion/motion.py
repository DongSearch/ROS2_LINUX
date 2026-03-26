import rclpy
from  rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import time
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class HumanMotion(Node):
    def __init__(self):
        super().__init__("motion_walk")
        self.publisher = self.create_publisher(JointState,"joint_states",10)
        self.timer = self.create_timer(0.1,self.update)
        self.t = 0.0
        self.br = TransformBroadcaster(self)

    def update(self) :
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [
            'left_shoulder',
            'right_shoulder',
            'left_hip',
            'right_hip'
        ]

        msg.position = [
            math.sin(self.t),
            -math.sin(self.t),
            -math.sin(self.t),
            math.sin(self.t)
        ]

        self.publisher.publish(msg)
        self.t += 0.1

        t = TransformStamped()
        t.header.stamp =  self.get_clock().now().to_msg()
        t.header.frame_id = "odom"
        t.child_frame_id = "torso"

        t.transform.translation.x = self.t * 0.05
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.br.sendTransform(t)

def main():
    rclpy.init()
    node = HumanMotion()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()