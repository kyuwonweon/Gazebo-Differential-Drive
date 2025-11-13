"""
Flip node for the car robot.

Makes the robot move back and forth along a line by
flipping over itself rather than turning.
"""
from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node


class Flip(Node):
    """
    Node to flip the car as it moves back and forth.

    PUBLISHES
    ----------
    /publisher (geometry_msgs.msg.Twist)
        Velocity command for the robot.
    """

    def __init__(self):
        """Initialize flip node."""
        super().__init__('flip')
        # Publisher for the cmd_vel topic
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.drive_speed = 3.0
        self.flip_time = 7.0
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.flip_timer = self.create_timer(self.flip_time,
                                            self.flip_callback)

    def timer_callback(self):
        """Timer callback."""
        msg = Twist()
        msg.linear.x = -self.drive_speed
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)

    def flip_callback(self):
        """Flip callback."""
        self.drive_speed = -self.drive_speed


def main(args=None):
    """Intialize, spins, and shutds down ros2 node."""
    rclpy.init(args=args)
    node = Flip()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
