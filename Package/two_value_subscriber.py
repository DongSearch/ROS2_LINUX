import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MySubscriber(Node):

    def __init__(self):
        super().__init__('my_subscriber')

        self.subscription = self.create_subscription(
            Int32MultiArray,
            'ab_topic',
            self.callback,
            10
        )
    
    def callback(self,msg):
        a = msg.data[0]
        b = msg.data[1]

        self.get_logger().info(f"a={a}, b={b}, sum={a+b}")

def main():
    rclpy.init()
    node = MySubscriber()
    rclpy.spin(node)
    node.destroy_node
    rclpy.shutdown

if __name__=='__main__':
    main()