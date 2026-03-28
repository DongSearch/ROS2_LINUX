import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from turtle_interfaces.action import MoveTo
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from rclpy.executors import MultiThreadedExecutor


class TurtleServer(Node):
    def __init__(self) :
        super().__init__("turtlecli")
        self.publisher = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.server = ActionServer(self,MoveTo,'move',self.execute_callback)
        self.pose = None
        self.sub_pos = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)


    def pose_callback(self,msg):
        self.pose = msg


    def execute_callback(self,goal_handle) :
        self.get_logger().info(f"Received goal : x={goal_handle.request.x} , y= {goal_handle.request.y}")
        feedback_msg = MoveTo.Feedback()
        rate = self.create_rate(10) # 10 Hz

        tx = goal_handle.request.x
        ty = goal_handle.request.y

        while rclpy.ok(): # check if node is activating correctly
            if self.pose is None :
                rate.sleep() # restrict loop for avoding to use too much memory
                continue
        
            dx = tx - self.pose.x
            dy = ty - self.pose.y
            distance = math.sqrt(dx**2 + dy**2)
            feedback_msg.current_x = self.pose.x
            feedback_msg.current_y = self.pose.y
            goal_handle.publish_feedback(feedback_msg)

            if distance < 0.1:
                break

            cmd = Twist()
            cmd.linear.x = min(1.0,1.5 * distance)
            angle = (math.atan2(dy,dx) - self.pose.theta)
            cmd.angular.z = 4* self.normalize_angle(angle)
            self.publisher.publish(cmd)

            rate.sleep()

        self.publisher.publish(Twist()) # stop
        goal_handle.succeed()
        result = MoveTo.Result()
        result.success = True
        return result
    def normalize_angle(self,angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi :
            angle += 2.0 * math.pi
        return angle
    
def main(args=None):
    rclpy.init(args=args)
    server = TurtleServer()
    executor = MultiThreadedExecutor()
    executor.add_node(server)
    executor.spin()
    server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


