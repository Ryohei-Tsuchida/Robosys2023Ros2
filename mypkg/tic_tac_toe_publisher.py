import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TicTacToePublisherNode(Node):

    def __init__(self):
        super().__init__('tic_tac_toe_publisher')
        self.publisher_ = self.create_publisher(String, 'tic_tac_toe', 10)
        self.timer_ = self.create_timer(1, self.publish_message)
        self.board = [' '] * 9  # Initialize an empty tic-tac-toe board
        self.current_player = 'X'  # Player X starts

    def publish_message(self):
        msg = String()
        msg.data = self.get_board_string()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)
        self.check_winner()

    def get_board_string(self):
        return '\n'.join([' '.join(self.board[i:i+3]) for i in range(0, 9, 3)])

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                self.get_logger().info('Player %s wins!' % self.current_player)
                rclpy.shutdown()

        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                self.get_logger().info('Player %s wins!' % self.current_player)
                rclpy.shutdown()

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.get_logger().info('Player %s wins!' % self.current_player)
            rclpy.shutdown()

        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.get_logger().info('Player %s wins!' % self.current_player)
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = TicTacToePublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

