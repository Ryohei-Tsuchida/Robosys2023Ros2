#!/bin/bash
# SPDX-FileCopyrightText:2023 Ryohei Tsuchida
# SPDX-License-Identifier:BSD-3-Clau

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 40 ros2 launch mypkg randam_number_ans.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Time up! The answer is:'
