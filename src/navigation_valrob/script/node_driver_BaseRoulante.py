#!/usr/bin/python3

# @author S6ril & Starfunx


"""
Cette node permet de communiquer avec le robot en Gcode

"""


import rospy
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

from Communication_gcode import Communication_Gcode
import serial

def communication():
    """
    Fonction principale de la node, elle permet de communiquer avec le robot

    """
    rospy.init_node('communication', anonymous=True)
    driver_robot = Communication_Gcode("/dev/ttyACM0", 9600)

    pub_pose = rospy.Publisher('/turtle1/pose', Pose2D, queue_size=10)
    rospy.Subscriber('/turtle1/cmd_vel', Twist, driver_robot.set_robot_speed)

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        pub_pose.publish(driver_robot.get_robot_pose())
        rate.sleep()

    del driver_robot


if __name__ == '__main__':
    try:
        communication()
    except rospy.ROSInterruptException:
        pass