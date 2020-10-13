#!/usr/bin/env python
import rospy
from problem_no1.srv import requestdata_p3


''' def handle(req):
	rospy.loginfo("Request received")
	rospy.loginfo("Entered data:")
	rospy.loginfo(req)
	availibility = False
	xt = target_x
	yt = target_y
	ls = [availibility, xt, yt]
	return ls
 '''

 
if __name__ == '__main__':
	rospy.init_node("server_p3")
	rospy.loginfo("Server started")
	target_x = input("Enter x: ")
	target_y = input("Enter y: ")

try:
	
	request_data = rospy.ServiceProxy("/data_request_p3", requestdata_p3)
	response = request_data("SendData")
	rospy.loginfo("Response data: ")
	rospy.loginfo(response)
	rospy.spin()
# if the robot is available server does task allocation algorithm and sends back data(ava. , xt , yt) 
# and waits for robot finish report
	#if response.availibility == True"



except rospy.ServiceException as e:
	rospy.logwarn("Service Failed" , str(e))


	#service = rospy.Service("/data_request", servicedata, handle)	
	#rospy.spin()
