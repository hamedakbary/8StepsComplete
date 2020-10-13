#!/usr/bin/env python
import rospy
from problem_no1.srv import requestdata_p3


id = 50
type = "turtle"
availibility = True
robot_x = 1.1
robot_y = 4.6


def handle(req):
	rospy.loginfo("Request received")
	rospy.loginfo("Data proceessing ...")
	avail = availibility
	idnum = id
	xr = robot_x
	yr = robot_y
	ls = [avail, idnum, xr, yr]
	return ls



if __name__ == '__main__':
	rospy.init_node("client2_p3")
#rospy.wait_for_service("/data_request")
	service = rospy.Service("/data_request_p3", requestdata_p3, handle)	
	rospy.spin()


''' try:
	
	request_data = rospy.ServiceProxy("/data_request", servicedata)
	response = request_data(id, type, availibility , round(xr,2), round(yr,2))
	rospy.loginfo("Response data: ")
	rospy.loginfo(response)
except rospy.ServiceException as e:
		rospy.logwarn("Service Failed" , str(e)) '''

	
