import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MyPublisher(Node):

    def __init__(self):
        super().__init__('my_publisher')
        self.publisher = self.create_publisher(Int32MultiArray, 'ab_topic',10)
        self.a = 0
        self.b = 0

        self.timer_a = self.create_timer(0.5, self.update_a)
        self.timer_b = self.create_timer(2, self.update_b)
        self.timer_pub = self.create_timer(0.5,self.publish_msg)

    def update_a(self):
        self.a +=1
    
    def update_b(self):
        self.b +=1

    def publish_msg(self):
        msg = Int32MultiArray()
        msg.data = [self.a,self.b]
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()
