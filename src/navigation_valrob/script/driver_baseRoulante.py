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
        self.ser = serial.Serial()
        self.ser.port = portserial
        self.ser.baudrate = bauderate
        self.ser.timeout = 0
        self.ser.open()

    def __del__(self):
        self.ser.close()
        print("serial close")

    # Commandes déplacements:
    def set_fast_move_to(self, x, y, theta):
        self.ser.write(b'G00 X')
        self.ser.write(str.encode(str(x)))
        self.ser.write(b' Y')
        self.ser.write(str.encode(str(y)))
        self.ser.write(b' A')
        self.ser.write(str.encode(str(theta)))

    def set_slow_move_to(self, x, y, theta):
        self.ser.write(b'G01 X')
        self.ser.write(str.encode(str(x)))
        self.ser.write(b' Y')
        self.ser.write(str.encode(str(y)))
        self.ser.write(b' A')
        self.ser.write(str.encode(str(theta)))

    def set_robot_speed(self, linear, angular):
        self.ser.write(b'G10 I')
        self.ser.write(str.encode(str(linear)))
        self.ser.write(b' J')
        self.ser.write(str.encode(str(angular)))

    def set_robot_wheel_speed(self, leftWheelSpeed, RightWeelSpeed):
        self.ser.write(b'G11 I')
        self.ser.write(str.encode(str(leftWheelSpeed)))
        self.ser.write(b' J')
        self.ser.write(str.encode(str(RightWeelSpeed)))

    # position control
    def get_robot_pose(self):
        """Fonction qui met à jour la position actuelle du robot dans la classe.

        :param robotPose: Position actuelle du robot.
        :type robotPose: Pose()
        """
        if (self.ser.is_open):
            self.ser.write(b'M114')
            message = self.ser.read(190) #read 50 bytes
            print("message =", message)
            if (len(message) > 4):
                indexX = message.index("X")
                indexY = message.index("Y")
                indexA = message.index("A")

                self.robotPose.x = float(message[ indexX+1: indexY ] )
                self.robotPose.y = float(message[ indexY+1: indexA ] )
                self.robotPose.theta = float(message[ indexA+1: ] )

        return self.robotPose

    def set_robot_pose(self, x, y, theta):
        self.ser.write(b'G92 X')
        self.ser.write(str.encode(str(x)))
        self.ser.write(b' Y')
        self.ser.write(str.encode(str(y)))
        self.ser.write(b' A')
        self.ser.write(str.encode(str(theta)))

    # motor enable control
    def enable_motors(self):
        if (self.ser.is_open):
            self.ser.write(b'M19') #Mise en route des moteurs

    def disable_motors(self):
        if (self.ser.is_open):
            self.ser.write(b'M18') #Stop tous les moteurs

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

    def set_odom_wheel_dist(self, d):
        pass

    def set_odom_wheel_dist(self, d):
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
        enable_motors()

    def stopRobot(self):
        disable_motors()
