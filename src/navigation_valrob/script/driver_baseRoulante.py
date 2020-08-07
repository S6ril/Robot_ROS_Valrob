# coding: utf-8
# @author S6ril & Starfunx

"""
Cette classe permet de gérer la communication Gcode

"""

from geometry_msgs.msg import Twist, Pose2D, Pose
import serial
import time

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
        """
        Destructeur de la classe.
        Permet de fermer le port Serial.
        """
        self.serial.close()
        print("serial close")

    def cleanSerial(self):
        """
        Nettoyage du buffer pour éviter une saturation.
        """
        self.serial.flushInput()
        self.serial.flushOutput()


    # Commandes déplacements:
    def set_fast_move_to(self, x: float, y: float, theta: float):
        """
        G00 Le robot se déplace au plus vite vers la cible et prends l’angle d’arrivée.

        :param x: Position en X absolue sur le terrain
        :type x: float
        :param y: Position en Y absolue sur le terrain
        :type y: flaot
        :param theta: Angle d'arrivé à prendre lorsque la position est atteinte
        :type theta: float
        """
        self.serial.write(b'G00 X')
        self.serial.write(str.encode(str(x)))
        self.serial.write(b' Y')
        self.serial.write(str.encode(str(y)))
        self.serial.write(b' A')
        self.serial.write(str.encode(str(theta)))
        self.serial.write(b'\n')

        self.cleanSerial()



    def set_slow_move_to(self, x: float, y: float, theta: float):
        """
        G01 Le robot se déplace vers la cible de façon linéaire : il s’oriente d’abord vers sa cible
        avant d’avancer jusqu’à atteindre la cible. Il prend l’angle d’arrivée une fois sur la cible.
        
        :param x: Position en X absolue sur le terrain
        :type x: float
        :param y: Position en Y absolue sur le terrain
        :type y: flaot
        :param theta: Angle d'arrivé à prendre lorsque la position est atteinte
        :type theta: float
        """
        self.serial.write(b'G01 X')
        self.serial.write(str.encode(str(x)))
        self.serial.write(b' Y')
        self.serial.write(str.encode(str(y)))
        self.serial.write(b' A')
        self.serial.write(str.encode(str(theta)))
        self.serial.write(b'\n')

        self.cleanSerial()



    def set_robot_speed(self, linearSpeed: float, angularSpeed: float):
        """
        G10 Le robot se déplace à la vitesse et vitesse angulaire précisée.

        :param linearSpeed: Consigne en vitesse linéaire du robot
        :type linearSpeed: float
        :param angularSpeed: Consigne en vitesse angulaire du robot
        :type angularSpeed: float
        """
        self.serial.write(b'G10 I')
        self.serial.write(str.encode(str(linearSpeed)))
        self.serial.write(b' J')
        self.serial.write(str.encode(str(angularSpeed)))
        self.serial.write(b'\n')

        self.cleanSerial()



    def set_robot_wheel_speed(self, leftWheelSpeed: float, RightWeelSpeed: float):
        """
        G11 Les roues du robot se déplacent aux vitesses précisées.

        :param leftWheelSpeed: Consigne de vitesse de la roue gauche
        :type leftWheelSpeed: float
        :param RightWeelSpeed: Consigne de vitesse de la roue droite
        :type RightWeelSpeed: float
        """
        self.serial.write(b'G11 I')
        self.serial.write(str.encode(str(leftWheelSpeed)))
        self.serial.write(b' J')
        self.serial.write(str.encode(str(RightWeelSpeed)))
        self.serial.write(b'\n')

        self.cleanSerial()



    # position control
    def get_robot_pose(self) -> Pose2D:
        """
        Fonction qui met à jour la position actuelle du robot dans la classe.
        

        :param robotPose: Position actuelle du robot.
        :type robotPose: Pose2D
        """
        if (self.serial.is_open):
            self.serial.write(b'M114\n') # Demande la position au robot

            message = self.serial.readlines() # Lecture du port serial

            # print("message =", message)
            if (len(message) > 0):
                message = message[0].decode() #Conversion bytes en str
                message = message.rstrip()  #Enlève \n
                message = message.split(" ")    #Conversion str en list

                # Répartition des valeurs dans la variable position.
                self.robotPose.x = float(message[ 1 ] )
                self.robotPose.y = float(message[ 3 ] )
                self.robotPose.theta = float(message[ 5 ] )

            self.cleanSerial()
        return self.robotPose



    def set_robot_pose(self, x: float, y: float, theta: float):
        """
        G92 Met à jour la position du robot, et change place la consigne de position du robot 
        à la même valeur.

        :param x: Nouvelle valeur de position suivant l'axe x
        :type x: float
        :param y: Nouvelle valeur de postion suivant l'axe y
        :type y: float
        :param theta: Nouvelle valeur de position autour de l'axe z
        :type theta: float
        """
        self.serial.write(b'G92 X')
        self.serial.write(str.encode(str(x)))
        self.serial.write(b' Y')
        self.serial.write(str.encode(str(y)))
        self.serial.write(b' A')
        self.serial.write(str.encode(str(theta)))
        self.serial.write(b'\n')

        self.cleanSerial()



    # motor enable control
    def enable_motors(self):
        """
        M19 Active les moteurs et remet à zéro les intégrateurs des PID de contrôle moteur
        """
        if (self.serial.is_open):
            self.serial.write(b'M19\n') #Mise en route des moteurs

            self.cleanSerial()



    def disable_motors(self):
        """
        M18 Désactive les déplacements moteurs stoppant les mouvements jusqu’à réactivation 
        via la commande M19
        """
        if (self.serial.is_open):
            self.serial.write(b'M18\n') #Stop tous les moteurs

            self.cleanSerial()



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
    
    def set_robot_speed_ros(self, msg_twist: Twist ):
        """
        Aliase de la fonction set robot speed. Cela permet de garder une cohérence des commandes 
        et d'avoir des fonctions spéciales ROS

        :param msg_twist: Commande de vitesse ROS
        :type msg_twist: Twist
        """
        self.set_robot_speed(msg_twist.linear.x, msg_twist.angular.z)


