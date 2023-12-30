import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from time import time

class RandomAnswerSubscriber(Node):
    def __init__(self):
        super().__init__('random_ans')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'random_numbers',
            self.callback,
            10)
        self.subscription  # prevent unused variable warning
        self.start_time = None
        self.answered = False  # Flag to track if an answer has been provided
        self.last_received_numbers = None
        self.timer_ = self.create_timer(30.0, self.timer_callback)  # 30秒ごとに実行

    def callback(self, msg):
        if self.answered:
            return

        if self.start_time is None:
            self.start_time = time()
            self.last_received_numbers = msg.data

        elapsed_time = time() - self.start_time
        if elapsed_time < 30:
            print("Select a prime number from the following list:")
            print(self.last_received_numbers)

    def timer_callback(self):
        if not self.answered and self.last_received_numbers is not None:
            self.answered = True  # Set the flag to indicate that an answer has been provided
            print("Time up!")
            print("The answer is:")
            prime_numbers = [num for num in self.last_received_numbers if self.is_prime(num)]
            print(prime_numbers)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

def main(args=None):
    rclpy.init(args=args)
    random_ans_subscriber = RandomAnswerSubscriber()
    rclpy.spin(random_ans_subscriber)
    random_ans_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

