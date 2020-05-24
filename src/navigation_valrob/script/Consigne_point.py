# coding: utf-8
"""
@license
@author S6ril & Starfunx
"""

from math import sqrt, pow, atan2, cos, sin
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

# from Nav_utiles import *


class Consigne_Point(object):
    """docstring for Consigne_Point."""

    def __init__(self, distance_tolerance, angle_tolerance, maxLinVelStopped, maxAngVelStopped):
        super(Consigne_Point, self).__init__()
        self.listCoord = []

        self.distance_tolerance = distance_tolerance
        self.angle_tolerance = angle_tolerance
        self.maxLinVelStopped = maxLinVelStopped
        self.maxAngVelStopped = maxAngVelStopped

    def update_robot_consign(self):
        pass


    def lecture_fichier(self, nomFichier):
        fichier = open(nomFichier, "r")

        line = fichier.readline()
        while line != "":
            self.listCoord.append([float(x) for x in line.split(" ")])
            line = fichier.readline()

        fichier.close()
