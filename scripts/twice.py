#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def cb(message):
 rospy.loginfo("Hello World%s",message,data)
if _i_name__ == '__main__':
 rospy.init_node('twice')
 sub = rospy.Subscriber('count_up', String, cb)
 rospy.spin()
