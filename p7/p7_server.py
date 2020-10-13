#!/usr/bin/env python
import rospy
import os
from math import sqrt

from problem_no1.create_client import CreateClient
from problem_no1.srv import servicedata
from std_msgs.msg import String

def task_allocation_algorithm(robot_x, robot_y, target_x, target_y):
    d = sqrt((robot_x-target_x)**2+(robot_y-target_y)**2)
    return d


def handle(req):

    global min, idnum
    rospy.loginfo("\n")
    rospy.loginfo("Data Received:")
    rospy.loginfo(req)
    
    criteria = task_allocation_algorithm(req.xr, req.yr, xt, yt)
    rospy.loginfo(criteria)
    if criteria < min:
        min = criteria
        idnum = req.id

    availibility = False
    ls = [idnum, availibility, xt, yt]
    return ls
    


if __name__ == '__main__':

    rospy.init_node("p7_server")
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
                min = 100
                idnum = 1
                rospy.sleep(1)
                pub.publish(message)
                rospy.loginfo(message)
                rospy.sleep(num_of_clients + 1)
            except:
                rospy.loginfo("Enter correct number again!")

        elif action == 2:
            input_type = raw_input("Enter client type: ")
            my_client = CreateClient(num_of_clients + 1, input_type, True ,0 ,0)
            num_of_clients += 1

        elif action == 3:
            rospy.signal_shutdown("User")
            rospy.loginfo("Server has been Shut down")
        
        else:
            pass


