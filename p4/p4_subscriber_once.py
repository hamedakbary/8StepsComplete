#!/usr/bin/env python
import rospy
from problem_no1.msg import topicdata

def callback(msg):
	rospy.loginfo("message received: ")
	rospy.loginfo(msg)


if __name__ == '__main__':
	rospy.init_node('subscriber_once')
	sub = rospy.Subscriber("/publish_once", topicdata, callback)
	rospy.spin()

