import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import UInt32


class writernode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好,我是%s" %name)

        self.pub_money = self.create_publisher(UInt32, "money", 10)

        time_period = 0.01
        self.timer = self.create_timer(time_period,self.timer_callback)

        self.count = 0
        self.sub_novel = self.create_subscription(String, "book",self.recv_callback, 10)

    def timer_callback(self):

        msg = UInt32()
        msg.data = 30
        self.pub_money.publish(msg)
        self.get_logger().info("給作家%d元" %msg.data)

    def recv_callback(self, msg):
        self.get_logger().info("收到:%s這個訊息" %msg.data)

    
def main(args=None):
    rclpy.init(args=args)
    node = writernode("wang")  #注意不能用中文的
    rclpy.spin(node)
    rclpy.shutdown()
    





