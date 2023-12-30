#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 40 ros2 launch mypkg randam_number_ans.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Time up!'
