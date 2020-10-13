#!/usr/bin/env python
import rospy
import os
from problem_no1.srv import servicedata
from std_msgs.msg import String

class Create_Client():
    def __init__(self, id, type, availibility , xr , yr):
        self.id = id
        self.type = type
        self.availibility = availibility
        self.xr = xr
        self.yr = yr

        path = "/home/hamed2/catkin_ws/src/problem_no1/p6/"
        file_name = path + "p6_client" + str(id) + ".py"
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
            file.write("\n    rospy.loginfo(msg)")
            file.write("\n    request_data = rospy.ServiceProxy(\"/data_exchange\", servicedata)")
            file.write("\n    rospy.sleep(id)")
            file.write("\n    response = request_data(id, type, availibility , round(xr,2), round(yr,2))")
            file.write("\n    rospy.loginfo(\"Response Received\")")
            file.write("\n    if response.id == id:")
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


def handle(req):
    rospy.loginfo("\n")
    rospy.loginfo("Data Received:")
    rospy.loginfo(req)
    idnum = 2
    availibility = False
    ls = [idnum, availibility, xt, yt]
    return ls
    


if __name__ == '__main__':
    rospy.init_node("p6_server")
    service = rospy.Service("/data_exchange", servicedata, handle)
    pub = rospy.Publisher("/publish_request", String, queue_size = 10)
    rospy.loginfo("Server initiated")
    num_of_clients = input("Enter the number of Robots: ")
   
            
    while not rospy.is_shutdown():
        rospy.loginfo("\n")
        rospy.loginfo("Actions:")
        rospy.loginfo("1.Enter Targets coordinates")
        rospy.loginfo("2.Create New Client")
        rospy.loginfo("3.Turn Off Server")
        action = input("Enter the action letter (1/2/3): ")

        if action == 1:
            try:
                xt = input("Enter x: ")
                yt = input("Enter y: ")
                message = "New target appeared. Waiting for clients data."
                rospy.sleep(1)
                pub.publish(message)
                rospy.loginfo(message)
                rospy.sleep(num_of_clients + 1)
            except:
                rospy.loginfo("Enter correct number again!")

        elif action == 2:
            input_type = raw_input("Enter client type: ")
            my_client = Create_Client(num_of_clients + 1, input_type, True ,0 ,0)
            num_of_clients += 1

        elif action == 3:
            rospy.signal_shutdown("User")
            rospy.loginfo("Server has been Stopped")
        
        else:
            pass


