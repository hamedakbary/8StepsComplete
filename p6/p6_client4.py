#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata
from std_msgs.msg import String

id = 4
type = "turtle"
availibility = True
xr = 0.00
yr = 0.00

def callback(msg):
    rospy.loginfo(msg)
    request_data = rospy.ServiceProxy("/data_exchange", servicedata)
    rospy.sleep(id)
    response = request_data(id, type, availibility , round(xr,2), round(yr,2))
    rospy.loginfo("Response Received")
    if response.id == id:
        rospy.loginfo("Response data: ")
        rospy.loginfo(response)
    else:
        rospy.loginfo("This client is free")

if __name__ == '__main__':
    rospy.init_node("p5_client4")
    rospy.wait_for_service("/data_exchange")
    sub = rospy.Subscriber("/publish_request", String, callback)
    rospy.spin()