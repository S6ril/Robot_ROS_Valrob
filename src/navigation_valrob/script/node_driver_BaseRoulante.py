#!/usr/bin/python3

# @author S6ril & Starfunx


"""
Cette node permet de communiquer avec le robot en Gcode. 
ELle récupère la consigne en vitesse et renvoie la position du robot.
"""


import rospy
from geometry_msgs.msg import Twist, Pose2D

from driver_baseRoulante import Communication_Gcode
import serial

def communication():
    """
    Fonction principale de la node, elle permet de communiquer avec le robot.
    Elle demande les valeurs dans le ROSLaunch :
        - portCarte : port où se trouve la carte
        - bauderate : bauderate de communication de la carte
    """

    # Récupération des paramètres du ROSLaunch
    portCarte = rospy.get_param('portCarte', 0)
    bauderate = rospy.get_param('bauderate', 0)

    # Initiation de la classe Communication
    driver_robot = Communication_Gcode("/dev/tty" + portCarte, bauderate)
    
    # Initiation des E/S ROS
    rospy.init_node('communication', anonymous=True)

    rospy.Subscriber('/robot/cmd_vel', Twist, driver_robot.set_robot_speed_ros) #Entrée
    pub_pose = rospy.Publisher('/robot/pose', Pose2D, queue_size=10) # Sortie

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # Publication de la sortie à 10Hz
        pub_pose.publish(driver_robot.get_robot_pose())
        rate.sleep()

    # Fermeture du port série
    del driver_robot


if __name__ == '__main__':
    try:
        communication()
    except rospy.ROSInterruptException:
        pass
