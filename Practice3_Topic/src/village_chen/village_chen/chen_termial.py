import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import UInt32

class writernode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好,我是%s" %name)
        self.pub_novel = self.create_publisher(String, "book", 10)

        self.count = 0
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.account = 60
        self.submoney = self.create_subscription(UInt32, "money", self.recv_callback,10)


    def timer_callback(self):
        msg = String()
        msg.data = "第%d次:chen 發布了第%d回小說" %(self.count,self.count)
        self.pub_novel.publish(msg)
        self.get_logger().info("%s" %msg.data)
        self.count += 1

    
    def recv_callback(self,money):
        self.account += money.data
        self.get_logger().info("chen 我收到了%d的錢了" %money.data)


def main(args=None):
    rclpy.init(args=args)
    node = writernode("chen")
    rclpy.spin(node)
    rclpy.shutdown()
