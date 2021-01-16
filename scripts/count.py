#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

 rospy.init_node('count')                                # ノード名「count」に設定
 pub = rospy.Publisher('count_up', String, queue_size=1)  # パブリッシャ「count_up」を作成
 rate = rospy.Rate(1)                                   # 1Hzで実行

while not rospy.is_shutdown():
 rospy.loginfo("Hello World")       
 pub.publish()
 rate.sleep()
