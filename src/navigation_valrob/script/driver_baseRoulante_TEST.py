# coding: utf-8
# @author S6ril & Starfunx

"""
Cette classe permet de gérer la communication Gcode

"""

from geometry_msgs.msg import Twist, Pose2D, Pose
import serial

import rospy

class Communication_Gcode(object):
    """
    Classe driver de la carte d'asservissement base roulante
    gère la communication sur le port serial
    """

    def __init__(self, portserial, bauderate):
        super(Communication_Gcode, self).__init__()
        self.robotPose = Pose2D()
        self.ser = serial.Serial()
        self.ser.port = portserial
        self.ser.baudrate = bauderate
        self.ser.timeout = 0
        self.ser.open()

        self.ser.write(b'M666')

        self.speed_L = 0
        self.speed_R = 0

        self.isDriving = False

    def __del__(self):
        self.ser.close()
        print("serial close")

    def set_robot_speed(self, msg_twist):
        if msg_twist.linear.x == 1:
            self.isDriving = True
            self.set_robot_angular_speed(msg_twist)
        
        elif self.isDriving:
            self.ser.write(b'M18')
            self.ser.write(b'\n')
            self.isDriving = False
        
        elif msg_twist.linear.x == -1:
            self.isDriving = True
            msg_twist.angular.z = - msg_twist.angular.z
            self.set_robot_angular_speed(msg_twist)
        
        self.ser.flushInput()
        self.ser.flushOutput()


    def set_robot_angular_speed(self, msg_twist):
        # rospy.loginfo(msg_twist)

        self.speed_L = 150 - msg_twist.angular.z
        self.speed_R = 150 + msg_twist.angular.z
        
        self.ser.write(b'G11 I')
        self.ser.write(str.encode(str(int(self.speed_L))))
        self.ser.write(b' J')
        self.ser.write(str.encode(str(int(self.speed_R))))
        self.ser.write(b'\n')
