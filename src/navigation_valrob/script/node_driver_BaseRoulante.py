#!/usr/bin/python3

# @author S6ril & Starfunx


"""
Cette node permet de communiquer avec le robot en Gcode

"""


import rospy
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

from driver_baseRoulante_TEST import Communication_Gcode
import serial

def communication():
    """
    Fonction principale de la node, elle permet de communiquer avec le robot

    """
    rospy.init_node('communication', anonymous=True)
    driver_robot = Communication_Gcode("/dev/ttyACM1", 9600)

    rospy.Subscriber('/robot/cmd_vel', Twist, driver_robot.set_robot_speed)

    rate = rospy.Rate(1)  # 1hz
    while not rospy.is_shutdown():
        
        rate.sleep()

    del driver_robot


if __name__ == '__main__':
    try:
        communication()
    except rospy.ROSInterruptException:
        pass
