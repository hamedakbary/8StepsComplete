#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata
from std_msgs.msg import String


def handle(req):
    rospy.loginfo("\n")
    rospy.loginfo("Data Received:")
    rospy.loginfo(req)
    idnum = 01
    availibility = False
    ls = [idnum, availibility, xt, yt]
    return ls

if __name__ == '__main__':
    rospy.init_node("p5_server")
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
            xt = input("Enter x: ")
            yt = input("Enter y: ")
            message = "New target appeared. Waiting for clients data."
            rospy.sleep(1)
            pub.publish(message)
            rospy.loginfo(message)
            rospy.sleep(num_of_clients + 1)

        elif action == 2:
            pass

        elif action == 3:
            rospy.signal_shutdown("User")
            rospy.loginfo("Server has been Stopped")


