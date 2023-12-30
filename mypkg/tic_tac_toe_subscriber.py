import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TicTacToeSubscriberNode(Node):

    def __init__(self):
        super().__init__('tic_tac_toe_subscriber')
        self.subscription_ = self.create_subscription(
            String,
            'tic_tac_toe',
            self.listener_callback,
            10)
        self.subscription_

    def listener_callback(self, msg):
        self.get_logger().info('Received:\n%s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = TicTacToeSubscriberNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

