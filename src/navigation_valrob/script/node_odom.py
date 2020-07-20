#!/usr/bin/python3

# @author S6ril & Starfunx


"""
Cette node permet de gérer les déplacements du robot. Elle vérifie que le robot se dirige bien vers la consigne demandée.

"""


import rospy
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose
from math import sqrt, pow, atan2, cos, sin

from odom import Odometer


def odom():
    
    rospy.init_node('odometrie', anonymous=True)

    odometer = Odometer(0x046d, 0xc018)

    pub_odometrie = rospy.Publisher('/turtle1/cmd_vel', Pose2D, queue_size=10)

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        odometer.read_speed()
        print(odometer.robotPose)
        pub_odometrie.publish(odometer.robotPose)
        rate.sleep()


if __name__ == '__main__':
    try:
        odom()
    except rospy.ROSInterruptException:
        pass