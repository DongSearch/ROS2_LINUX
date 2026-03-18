import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from std_msgs.msg import Float32
from rclpy.action import ActionClient
from my_robot_interfaces.action import SwitchControl

class ManagerNode(Node):
    def __init__(self):
        super().__init__("manager_node")
        self.subscriber = self.create_subscription(
            Float32, "temperature", self.temp_callback,10
        )
        self.cooler_client = self.create_client(SetBool,"cooler_motor")
        self.swtich_client = ActionClient(self, SwitchControl, 'switch_control')
        self.is_changed = False

    def temp_callback(self,msg):
        temp = msg.data
        self.get_logger().info(f"Received temperature : {temp:.2f}")
        flag = "True" if temp > 30 else "False"
        if  flag !=  self.is_changed :
            self.call_cooler_service(turn_on=flag)
            self.is_changed = flag
        self.send_switch_goal(flag)

    def call_cooler_service(self,turn_on):
        while not self.cooler_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Waiting for cooler_motoer service....")
        req = SetBool.Request()
        flag = True if turn_on == "True" else False
        req.data = flag
        future = self.cooler_client.call_async(req)
        future.add_done_callback(
            lambda f : self.get_logger().info("Cooler service called.")
        )
    def send_switch_goal(self,turn_on):
        if not self.swtich_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().warn("Switch control arction server not available")
            return
        goal_msg = SwitchControl.Goal()
        goal_msg.turn_on = turn_on
        self.swtich_client.send_goal_async(goal_msg)

    
def main():
    rclpy.init()
    rclpy.spin(ManagerNode())
    rclpy.shutdown()

    if __name__ =="__main__":
        main()