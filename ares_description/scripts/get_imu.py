#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 参考自https://zhuanlan.zhihu.com/p/62607472
import rospy
import math
from sensor_msgs.msg import Imu

def imu_data(imu_data):

    # Read the angular velocity of the robot IMU
    w_x = imu_data.angular_velocity.x
    w_y = imu_data.angular_velocity.y
    w_z = imu_data.angular_velocity.z

    # Read the linear acceleration of the robot IMU
    a_x = imu_data.linear_acceleration.x
    a_y = imu_data.linear_acceleration.y
    a_z = imu_data.linear_acceleration.z
    
    # Read the quaternion of the robot IMU
    x = imu_data.orientation.x
    y = imu_data.orientation.y
    z = imu_data.orientation.z
    w = imu_data.orientation.w

    # Convert Quaternions to Euler-Angles
    rpy_angle = [0, 0, 0]
    rpy_angle[0] = math.atan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))
    rpy_angle[1] = math.asin(2 * (w * y - z * x))
    rpy_angle[2] = math.atan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))
    return

if __name__ == '__main__':
    rospy.init_node('imu_data', anonymous=True)
    rospy.Subscriber("/imu", Imu, imu_data)
    rospy.spin()