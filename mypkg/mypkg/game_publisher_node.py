import rclpy
from rclpy.node import Node
from othello.msg import GameState

class GamePublisherNode(Node):
    def __init__(self):
        super().__init__('game_publisher_node')
        self.publisher = self.create_publisher(GameState, 'game_state', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_game_state)

    def publish_game_state(self):
        # 仮のゲーム状態を生成
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        is_black_turn = True
        msg = GameState()
        msg.board = board
        msg.is_black_turn = is_black_turn
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    game_publisher_node = GamePublisherNode()
    rclpy.spin(game_publisher_node)
    game_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

