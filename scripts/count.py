#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('count')                                # ノード名「count」に設定
pub = rospy.Publisher('count_up', Int32, queue_size=1)  # パブリッシャ「count_up」を作成
rate = rospy.Rate(1)                                    #1Hzで実行
n = 0
while not rospy.is_shutdown():
    print("入力された数字が足されます。")
    a = int(input())
    n += a
    pub.publish(n)
    rate.sleep()
