#!/usr/bin/python3

# @author S6ril & Starfunx


"""
Cette node permet de gérer les déplacements du robot. Elle vérifie que le robot se dirige bien vers la consigne demandée.

"""


import rospy
from geometry_msgs.msg import Twist, Pose2D

from math import sqrt, pow, atan2, cos, sin

from Motion_controller import Motion_controller


def motion_controller():
    """    
    Fonction principale de la node motion_controller.
    Elle demande des paramètres du roslaunch :
    
    - krho
    - kalpha
    """
    # Demande de paramètres du ROSLaunch
    krho = rospy.get_param('krho', 0)
    kalpha = rospy.get_param('kalpha', 0)

    # Initiation de la classe motion_controlleur
    motion_controller = Motion_controller(krho, kalpha )

    # Initiation de ROS
    rospy.init_node('motion_controller', anonymous=True)
    
    rospy.Subscriber("/robot/pose", Pose2D, motion_controller.update_robot_pos) # Entrée
    rospy.Subscriber("/robot/consign", Pose2D, motion_controller.update_robot_consign) # Entrée
    pub_cmd_Vel = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10) # Sortie

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # Publication de la sortie à 10Hz
        pub_cmd_Vel.publish(motion_controller.update_command_vel())
        rate.sleep()



if __name__ == '__main__':
    try:
        motion_controller()
    except rospy.ROSInterruptException:
        pass
