import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class StarPublish(Node):
    def __init__(self):
        super().__init__('start_pub')
        self.publisher = self.create_publisher(Twist,'turtle1/cmd_vel',10)
        self.time_period = 1.0
        self.timer = self.create_timer(self.time_period,self.draw_star_callback)
        self.state = "move"
        self.count = 0
   

    def draw_star_callback(self):
        msg = Twist()

        self.count %= 5
        if self.state == "move":
            msg.linear.x = 2.0
            time.sleep(2)
            self.state = "turn"
        elif self.state =="turn":
            msg.angular.z = -2.5 
            time.sleep(2)
            self.state = "move"
            self.count += 1
        
        
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = StarPublish()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


        

        