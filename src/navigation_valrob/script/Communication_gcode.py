# coding: utf-8

# @author S6ril & Starfunx


"""
Cette classe permet de gérer la communication Gcode

"""


from geometry_msgs.msg import Twist, Pose2D, Pose
import serial


class Communication_Gcode(object):
    """Classe pour gérer la communication
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

    def miseEnRouteRobot(self):
        if (self.ser.is_open):
            self.ser.write(b'M19') #Mise en route des moteurs

    def stopRobot(self):
        if (self.ser.is_open):
            self.ser.write(b'M18') #Stop tous les moteurs

    def commandeRobot(self, twist):
        self.ser.write(b'G10 I')
        self.ser.write(str.encode(str(twist.linear.x)))
        self.ser.write(b' J')
        self.ser.write(str.encode(str(twist.angular.z)))

