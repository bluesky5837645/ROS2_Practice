import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("li4")
    node.get_logger().info("大家好,我是作家李四")
    rclpy.spin(node)
    rclpy.shutdown()