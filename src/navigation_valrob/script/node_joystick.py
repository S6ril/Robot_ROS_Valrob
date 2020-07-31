#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist, Pose2D
from sensor_msgs.msg import Joy

from joystick import *


def joystick():
    rospy.init_node('joystick', anonymous=True)

    joystick = Joystick_driver()

    rospy.Subscriber('/joy', Joy, joystick.update_command_joy )
    pub_cmd_Vel = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10)


    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        pub_cmd_Vel.publish(joystick.update_command_vel() )
        rate.sleep()



if __name__ == '__main__':
    try:
        joystick()
    except rospy.ROSInterruptException:
        pass
