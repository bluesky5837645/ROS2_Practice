import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)
    node = Node("cheung")
    node.get_logger().info("大家好,我是cheung")
    rclpy.spin(node)
    rclpy.shutdown()
