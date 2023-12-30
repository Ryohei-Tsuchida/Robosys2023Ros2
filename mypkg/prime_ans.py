# SPDX-FileCopyrightText:2023 Ryohei Tsuchida
# SPDX-License-Identifier:BSD-3-Clau

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
            self.get_logger().info("Select a prime number from the following list:")
            self.get_logger().info(f"[{', '.join(map(str, self.last_received_numbers))}]")
        else:
            self.answered = True  # Set the flag to indicate that an answer has been provided
            self.timer_callback()

    def timer_callback(self):
        if not self.answered and self.last_received_numbers is not None:
            self.get_logger().info("Time up! The answer is:")
            prime_numbers = [num for num in self.last_received_numbers if self.is_prime(num)]
            if prime_numbers:
                self.get_logger().info(str(prime_numbers))
            else:
                self.get_logger().info("No prime numbers selected.")

            # Avoid recursive calls to timer_callback
            self.timer_.cancel()

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

    try:
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(random_ans_subscriber)
        rclpy.spin(random_ans_subscriber, executor=executor)
    except KeyboardInterrupt:
        pass

    random_ans_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

