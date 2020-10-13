#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata


def handle(req):
	rospy.loginfo("Request received")
	rospy.loginfo("Entered data:")
	rospy.loginfo(req)
	availibility = False
	xt = target_x
	yt = target_y
	ls = [req.id, availibility, xt, yt]
	return ls

if __name__ == '__main__':
	rospy.init_node("server")
	rospy.loginfo("Server started")
	target_x = input("Enter x: ")
	target_y = input("Enter y: ")
	service = rospy.Service("/data_request", servicedata, handle)	
	rospy.spin()
