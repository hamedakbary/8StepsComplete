#!/usr/bin/env python
import rospy
from problem_no1.msg import topicdata

if __name__ == '__main__':
	rospy.init_node('publisher_server')
	pub = rospy.Publisher("/command", topicdata, queue_size = 10)
	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		msg = topicdata()
		msg.id = 126
		msg.xt = 5.5
		msg.yt = 2
		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()
	rospy.loginfo("Stop")
