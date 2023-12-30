# SPDX-FileCopyrightText:2023 Ryohei Tsuchida
# SPDX-License-Identifier:BSD-3-Clau

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random

class RandomNumberPublisher(Node):
    def __init__(self):
        super().__init__('random_number')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'random_numbers', 10)
        self.timer_ = self.create_timer(30.0, self.publish_numbers)  # 30秒ごとに実行
        self.last_numbers = None
        self.publish_numbers()  # 初回は即座に実行

    def publish_numbers(self):
        numbers = self.generate_unique_numbers()
        msg = Int32MultiArray(data=numbers)
        self.publisher_.publish(msg)
        self.last_numbers = numbers

    def generate_unique_numbers(self):
        all_numbers = list(range(1, 101))
        random.shuffle(all_numbers)
        return all_numbers[:10]

def main(args=None):
    rclpy.init(args=args)
    random_number_publisher = RandomNumberPublisher()
    rclpy.spin_once(random_number_publisher)

if __name__ == '__main__':
    main()

