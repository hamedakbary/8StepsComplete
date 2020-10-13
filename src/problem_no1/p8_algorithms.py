#!/usr/bin/env python

import rospy
import os
import math

def algorithm1(robot_x, robot_y, target_x, target_y):
    d = math.sqrt((robot_x-target_x)**2+(robot_y-target_y)**2)
    return d