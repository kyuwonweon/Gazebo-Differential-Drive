"""
Flip node for the car robot.

Makes the robot move back and forth along a line by
flipping over itself rather than turning.
"""
import rclpy
from rclpy.node import Node


class Flip(Node):
    """
    Node to flip the car.

    Publishes
    """

    def __init__(self):
        """Initialize flip node."""
        return


def main(args=None):
    """Spin the node."""
    rclpy.init(args=args)
    node = Flip()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
