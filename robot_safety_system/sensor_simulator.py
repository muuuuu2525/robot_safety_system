# SPDX-FileCopyrightText: 2025 浅野真夢
# SPDX-License-Identifier: Apache-2.0

"""Obstacle detection sensor simulator."""

import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorSimulator(Node):
    """Publishes random distance data."""

    def __init__(self):
        """Initialize the node and publisher."""
        super().__init__('sensor_simulator')
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Sensor Simulator has started.')

    def timer_callback(self):
        """Publish distance data periodically."""
        msg = Float32()
        msg.data = round(random.uniform(0.5, 3.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing distance: {msg.data}m')


def main(args=None):
    """Run the main entry point."""
    rclpy.init(args=args)
    node = SensorSimulator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
