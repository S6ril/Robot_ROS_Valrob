# coding: utf-8
"""
@license
@author S6ril & Starfunx
"""

from math import sqrt, pow, atan2, cos, sin
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

from Nav_utiles import *


class Consigne_Point(object):
    """docstring for Consigne_Point."""

    def __init__(self, distance_tolerance, angle_tolerance, maxLinVelStopped, maxAngVelStopped, fichier):
        super(Consigne_Point, self).__init__()
        self.listCoord = []
        self.lecture_fichier(fichier)

        self.distance_tolerance = distance_tolerance
        self.angle_tolerance = angle_tolerance
        self.maxLinVelStopped = maxLinVelStopped
        self.maxAngVelStopped = maxAngVelStopped
        self.robotPose = Pose()
        self.robotConsign = Pose2D()



    def update_robot_pose(self, robotPose):
        self.robotPose = robotPose

    def send_new_consign(self):
        if isPosition_reached(self.robotPose, self.robotConsign, self.distance_tolerance):
            self.update_robot_consign()
        
        return self.robotConsign


    def update_robot_consign(self):
        if len(self.listCoord) > 0:
            consign = self.listCoord.pop(0) # Enleve et retourne le dernier élément de la liste
            self.robotConsign.x = consign[0]
            self.robotConsign.y = consign[1]
            self.robotConsign.theta = consign[2]
            print(consign)
        else:
            print("Pas de points supplémentaires")
            self.robotConsign.x = self.robotPose.x
            self.robotConsign.y = self.robotPose.y
            self.robotConsign.theta = self.robotPose.theta




    def lecture_fichier(self, nomFichier):
        fichier = open(nomFichier, "r")

        line = fichier.readline()
        while line != "":
            self.listCoord.append([float(x) for x in line.split(" ")])
            line = fichier.readline()

        print(self.listCoord)
        fichier.close()
