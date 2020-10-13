#!/usr/bin/env python
import rospy
from problem_no1.msg import topicdata

def callback(msg):
	rospy.loginfo("message received: ")
	rospy.loginfo(msg)


if __name__ == '__main__':
	rospy.init_node('robot')
	sub = rospy.Subscriber("/command", topicdata, callback)
	rospy.spin()

