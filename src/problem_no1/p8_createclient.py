#!/usr/bin/env python

import rospy
import os

class CreateClient():
    def __init__(self, id, type, availibility , xr , yr):
        self.id = id
        self.type = type
        self.availibility = availibility
        self.xr = xr
        self.yr = yr

        path = "/home/hamed2/catkin_ws/src/problem_no1/p8/clients/"
        file_name = path + "p8_client" + str(id) + ".py"
        if os.path.isfile(file_name) == False:
            file = open(file_name,"w")

            text1 = """#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata
from std_msgs.msg import String
from problem_no1.msg import clientdata
from problem_no1.msg import topicdata\n"""
            file.write(text1)
            file.write("\nid = ")
            file.write(str(id))
            file.write("\ntype = " + "\"" + type + "\"")


            text2 = """\navailibility = True
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
    rospy.loginfo("\\n")
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
    



if __name__ == '__main__':"""
            file.write(text2)
            file.write("\n    rospy.init_node(\"p8_client" + str(id) + "\")")


            text3 = """\n    sub_request = rospy.Subscriber("/publish_request", String, callback_request)
    sub_response = rospy.Subscriber("/publish_response", topicdata, callback_response)
    rospy.spin()"""
            file.write(text3)

            rospy.loginfo("File Created")
        else:
            rospy.loginfo("The file exists! Enter the number of robots correctly.")