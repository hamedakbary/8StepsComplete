#!/usr/bin/env python
import rospy
import os
from math import *
# import problem_no1.p8_algorithms
from problem_no1.p8_createclient import CreateClient
from problem_no1.msg import clientdata
from problem_no1.msg import topicdata
from std_msgs.msg import String

def task_allocation_algorithm(robot_x, robot_y, target_x, target_y):
    d = sqrt((robot_x-target_x)**2+(robot_y-target_y)**2)
    return d


def count_clients():
    currentdir = os.path.dirname(__file__)
    DIR = currentdir + "/clients/"
    path, dirs, files = next(os.walk(DIR))
    count = len(files)
    return count



def callback_data(data):

    global min, idnum
    rospy.loginfo("\n")
    rospy.loginfo("Data Received:")
    rospy.loginfo(data)

    if data.availibility == True:
        criteria = task_allocation_algorithm(data.xr, data.yr, xt, yt)
        rospy.loginfo(criteria)
        if criteria < min:
            min = criteria
            idnum = data.id

    


if __name__ == '__main__':

    rospy.init_node("p8_server")
    pub_request = rospy.Publisher("/publish_request", String, queue_size = 10)
    sub_data = rospy.Subscriber("/publish_data",clientdata , callback_data)
    rospy.loginfo("Server initiated")

    num_of_clients = count_clients()
    rospy.loginfo("The number of robots is: " + str(num_of_clients))

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
                pub_request.publish(message)
                rospy.loginfo(message)
                rospy.sleep(num_of_clients + 1)
                rospy.loginfo("\n")
                rospy.loginfo("The chosen robot id:" + str(idnum))
                pub_response = rospy.Publisher("/publish_response", topicdata, queue_size = 10)
                response = topicdata()
                response.id = idnum
                response.xt = xt
                response.yt = yt
                rospy.sleep(1)
                pub_response.publish(response)
                rospy.loginfo("Response sent!")
            except:
                rospy.loginfo("Enter correct number again!")

        elif action == 2:
            num_of_clients = count_clients()
            rospy.loginfo("The number of robots is: " + str(num_of_clients))
            input_type = raw_input("Enter client type: ")
            my_client = CreateClient(num_of_clients + 1, input_type, True ,0 ,0)
            num_of_clients += 1

        elif action == 3:
            # rospy.signal_shutdown("User")
            rospy.loginfo("Server has been Shut down")
            break
        
        else:
            pass


