#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata
from std_msgs.msg import String
from problem_no1.msg import clientdata
from problem_no1.msg import topicdata

id = 3
type = "turtle"
availibility = True
xr = 0.00
yr = 0.00

def callback_response(response):
    global availibility
    rospy.loginfo("Response received:")
    if response.id == id:
        availibility = False
        rospy.loginfo(response)
        rospy.loginfo("Moving toward target!")
    
    else:
        rospy.loginfo("This robot is free!")


def callback_request(msg):
    rospy.loginfo("\n")
    rospy.loginfo(msg)
    pub_data = rospy.Publisher("/publish_data", clientdata, queue_size = 10)
    data = clientdata()
    data.id = id
    data.availibility =availibility
    data.xr = xr
    data.yr = yr
    rospy.sleep(id)
    pub_data.publish(data)
    rospy.loginfo("Data sent. Waiting for response!")
    



if __name__ == '__main__':
    rospy.init_node("p8_client3")
    sub_request = rospy.Subscriber("/publish_request", String, callback_request)
    sub_response = rospy.Subscriber("/publish_response", topicdata, callback_response)
    rospy.spin()