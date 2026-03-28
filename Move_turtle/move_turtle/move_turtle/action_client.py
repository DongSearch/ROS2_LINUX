import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from turtle_interfaces.action import MoveTo

line =[(2.0,8.0), (5.0,5.0),(0.0,3.0)]
class TurtleClient(Node):
    def __init__(self):
        super().__init__("cli")
        self.cli = ActionClient(self,MoveTo,"move")
        while not self.cli.wait_for_server(timeout_sec=1) :
            self.get_logger().info("Waiting for Server")
        
        self.id = 0
        self.send_goal()


    def send_goal(self):
        goal = MoveTo.Goal()
        # x,y = map(float,input("please enter two integers :  ").split())
        self.id = (self.id+1) % 3
        x, y = line[self.id]
        goal.x = x
        goal.y = y
        self.goal_future = self.cli.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )
        self.goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self,feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"current position : ({feedback.current_x : .2f} , {feedback.current_y : .2f})")

    def goal_response_callback(self,future):
        goal_handle = future.result()
        if not goal_handle.accepted :
            self.get_logger().info("Goal rejected")
            return
        self.get_logger().info("Goal accepted")

        self.future_result = goal_handle.get_result_async()
        self.future_result.add_done_callback(self.result_callback)

    def result_callback(self,future):
        result  = future.result().result
        self.get_logger().info(f"Result : {result}")
        try:
            self.send_goal()
        except :
            self.get_logger.info("Exit")

def main(args=None):
    rclpy.init(args=args)
    server = TurtleClient()
    rclpy.spin(server)
    server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
