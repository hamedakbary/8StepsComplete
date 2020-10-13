#!/usr/bin/env python
import rospy
from problem_no1.msg import topicdata

if __name__ == '__main__':
    rospy.init_node('publisher_once')
    pub = rospy.Publisher("/publish_once", topicdata, queue_size = 10)
    msg = topicdata()
    msg.id = 126
    msg.xt = 5.5
    msg.yt = 2
    rospy.sleep(0.5)
    pub.publish(msg)
    rospy.loginfo(msg)
    rospy.spin()

rospy.loginfo("Stopped")