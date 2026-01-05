# SPDX-FileCopyrightText: 2025 浅野真夢
# SPDX-License-Identifier: Apache-2.0

"""Emergency stop system based on distance."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String


class SafetyBrake(Node):
    """Subscribes to distance and publishes safety status."""

    def __init__(self):
        """Initialize the node, subscriber, and publisher."""
        super().__init__('safety_brake')
        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'safety_status', 10)
        self.threshold = 1.0
        self.get_logger().info('[Safe]y Brake System is ready.')

    def listener_callback(self, msg):
        """Receive distance data and determine safety."""
        status_msg = String()
        if msg.data < self.threshold:
            self.get_logger().warn(f'DANGER! Distance: {msg.data}m. STOP!')
            status_msg.data = 'STOP'
        else:
            self.get_logger().info(f'[Safe] Distance: {msg.data}m. GO.')
            status_msg.data = 'GO'
        self.publisher_.publish(status_msg)


def main(args=None):
    """Run the main entry point."""
    rclpy.init(args=args)
    node = SafetyBrake()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
