import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__("sensor_node")
        self.publisher = self.create_publisher(Float32,"temperature",10)
        self.timer = self.create_timer(10,self.temperature_callback)

    def temperature_callback(self):
        temp = random.uniform(20.0,35.0)
        msg = Float32()
        msg.data = temp
        self.get_logger().info(f"publish temperature : {temp: .2f}")
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "_main__":
    main()