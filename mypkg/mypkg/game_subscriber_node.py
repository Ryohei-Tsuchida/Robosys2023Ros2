import rclpy
from rclpy.node import Node
from othello.msg import GameState

class GameSubscriberNode(Node):
    def __init__(self):
        super().__init__('game_subscriber_node')
        self.subscription = self.create_subscription(
            GameState, 'game_state', self.game_state_callback, 10)
        self.subscription  # prevent unused variable warning

    def game_state_callback(self, msg):
        # ゲーム状態を表示
        self.get_logger().info('Received game state:\nBoard: %s\nTurn: %s' % (msg.board, 'Black' if msg.is_black_turn else 'White'))

def main(args=None):
    rclpy.init(args=args)
    game_subscriber_node = GameSubscriberNode()
    rclpy.spin(game_subscriber_node)
    game_subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

