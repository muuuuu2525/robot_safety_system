import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class SensorSimulator(Node):
    def __init__(self):
        super().__init__('sensor_simulator')
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        distance = random.uniform(0.5, 3.0)
        msg = Float32()
        msg.data = distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing distance: {distance:.2f}m')


def main(args=None):
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
