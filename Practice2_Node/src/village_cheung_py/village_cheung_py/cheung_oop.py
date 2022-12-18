import rclpy
from rclpy.node import Node

class writernode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好,我是%s" %name) #格式化字串有很4種

def main(args=None):
    rclpy.init(args=args)
    node = writernode("cheung")
    rclpy.spin(node)
    rclpy.shutdown()







