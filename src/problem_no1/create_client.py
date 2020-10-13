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

        path = "/home/hamed2/catkin_ws/src/problem_no1/p7/clients/"
        file_name = path + "p7_client" + str(id) + ".py"
        if os.path.isfile(file_name) == False:
            file = open(file_name,"w")

            file.write("#!/usr/bin/env python")
            file.write("\nimport rospy")
            file.write("\nfrom problem_no1.srv import servicedata")
            file.write("\nfrom std_msgs.msg import String")
            file.write("\n")
            file.write("\nid = ")
            file.write(str(id))
            file.write("\ntype = " + "\"" + type + "\"")
            file.write("\navailibility = True")
            file.write("\nxr = 0.00")
            file.write("\nyr = 0.00")
            file.write("\n")
            file.write("\ndef callback(msg):")
            file.write("\n    global availibility")
            file.write("\n    rospy.loginfo(msg)")
            file.write("\n    request_data = rospy.ServiceProxy(\"/data_exchange\", servicedata)")
            file.write("\n    rospy.sleep(id)")
            file.write("\n    response = request_data(id, type, availibility , round(xr,2), round(yr,2))")
            file.write("\n    rospy.loginfo(\"Response Received\")")
            file.write("\n")
            file.write("\n    if response.id == id:")
            file.write("\n        availibility = response.availibility")
            file.write("\n        xt = response.xt")
            file.write("\n        yt = response.yt")         
            file.write("\n        rospy.loginfo(\"Response data: \")")
            file.write("\n        rospy.loginfo(response)")
            file.write("\n    else:")
            file.write("\n        rospy.loginfo(\"This client is free\")")
            file.write("\n")
            file.write("\nif __name__ == '__main__':")
            file.write("\n    rospy.init_node(\"p5_client" + str(id) + "\")")
            file.write("\n    rospy.wait_for_service(\"/data_exchange\")")
            file.write("\n    sub = rospy.Subscriber(\"/publish_request\", String, callback)")
            file.write("\n    rospy.spin()")
            rospy.loginfo("File Created")
        else:
            rospy.loginfo("The file exists! Enter the number of robots correctly.")