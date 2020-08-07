# coding: utf-8
# @author S6ril & Starfunx

"""
Cette classe permet de gérer la communication Gcode

"""

from geometry_msgs.msg import Twist, Pose2D, Pose
import serial

class Communication_Gcode(object):
    """
    Classe driver de la carte d'asservissement base roulante
    gère la communication sur le port serial
    """

    def __init__(self, portserial, bauderate):
        super(Communication_Gcode, self).__init__()
        self.robotPose = Pose2D()
        self.serial = serial.Serial()
        self.serial.port = portserial
        self.serial.baudrate = bauderate
        self.serial.timeout = 0
        self.serial.open()

    def __del__(self):
        self.serial.close()
        print("serial close")

    # Commandes déplacements:
    def set_fast_move_to(self, x, y, theta):
        self.serial.write(b'G00 X')
        self.serial.write(str.encode(str(x)))
        self.serial.write(b' Y')
        self.serial.write(str.encode(str(y)))
        self.serial.write(b' A')
        self.serial.write(str.encode(str(theta)))

    def set_slow_move_to(self, x, y, theta):
        self.serial.write(b'G01 X')
        self.serial.write(str.encode(str(x)))
        self.serial.write(b' Y')
        self.serial.write(str.encode(str(y)))
        self.serial.write(b' A')
        self.serial.write(str.encode(str(theta)))

    def set_robot_speed(self, msg_twist):
        self.serial.write(b'G10 I')
        self.serial.write(str.encode(str(msg_twist.linear.x)))
        self.serial.write(b' J')
        self.serial.write(str.encode(str(msg_twist.angular.z)))

    def set_robot_wheel_speed(self, leftWheelSpeed, RightWeelSpeed):
        self.serial.write(b'G11 I')
        self.serial.write(str.encode(str(leftWheelSpeed)))
        self.serial.write(b' J')
        self.serial.write(str.encode(str(RightWeelSpeed)))

    # position control
    def get_robot_pose(self):
        """Fonction qui met à jour la position actuelle du robot dans la classe.

        :param robotPose: Position actuelle du robot.
        :type robotPose: Pose()
        """
        if (self.serial.is_open):
            self.serial.write(b'M114')
            message = self.serial.read(190) #read 190 bytes
            print("message =", message)
            if (len(message) > 4):
                message = message.split(" ")
                print(message)

                self.robotPose.x = float(message[ 1 ] )
                self.robotPose.y = float(message[ 3 ] )
                self.robotPose.theta = float(message[ 5 ] )

        return self.robotPose

    def set_robot_pose(self, x, y, theta):
        self.serial.write(b'G92 X')
        self.serial.write(str.encode(str(x)))
        self.serial.write(b' Y')
        self.serial.write(str.encode(str(y)))
        self.serial.write(b' A')
        self.serial.write(str.encode(str(theta)))

    # motor enable control
    def enable_motors(self):
        if (self.serial.is_open):
            self.serial.write(b'M19') #Mise en route des moteurs

    def disable_motors(self):
        if (self.serial.is_open):
            self.serial.write(b'M18') #Stop tous les moteurs

    # tests commands
    def get_left_wheel_data(self):
        pass # to do ( besoin pour calibrer les pid avec zigler nichhols etc..)

    def get_right_wheel_data(self):
        pass # to do ( besoin pour calibrer les pid avec zigler nichhols etc..)

    #reglages paramètres
    def set_pid_left(self, p, i, d): # set pid vitesse gauche
        pass

    def set_pid_right(self, p, i, d): # set pid vitesse droite
        pass

    def set_left_odom_wheel_diameter(self, r):
        pass

    def set_right_odom_wheel_diameter(self, r):
        pass

    def set_odom_wheel_dist_left(self, d):
        pass

    def set_odom_wheel_dist_right(self, d):
        pass

    def set_max_linear_acceleration(self, value):
        pass

    def set_max_angular_acceleration(self, value):
        pass

    def set_max_linear_deceleration(self, value):
        pass

    def set_max_angular_deceleration(self, value):
        pass


    # aliases
    def miseEnRouteRobot(self):
        self.enable_motors()

    def stopRobot(self):
        self.disable_motors()
