import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import UInt32


class writernode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好,我是%s" %name)

        self.count = 0
        self.pub_novel = self.create_publisher(String, "book", 10)

        time_period = 1
        self.timer = self.create_timer(time_period,self.timer_callback)

        self.money = 50
        self.submoney = self.create_subscription(UInt32, "money",self.recv_callback, 10)

    def timer_callback(self):

        msg = String()
        msg.data = "作者發布第%d章節的小說" %self.count
        self.pub_novel.publish(msg)
        self.get_logger().info("%s" %msg.data)
        self.count += 1

    def recv_callback(self, money):
        self.money +=  money
        self.get_logger().info("作者收到%d元" %money)

    
def main(args=None):
    rclpy.init(args=args)
    node = writernode("chen")  #注意不能用中文的
    rclpy.spin(node)
    rclpy.shutdown()
    





