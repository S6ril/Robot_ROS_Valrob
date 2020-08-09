# coding: utf-8

# @author S6ril & Starfunx


"""
Cette classe permet de gérer les consignes données au robot.

"""


from math import sqrt, pow, atan2, cos, sin
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

from Nav_utiles import isPosition_reached


class Consigne_Point(object):
    """Classe pour gérer la consigne vers un point.
    Dès que le robot a atteind son objectif, une nouvelle consigne est générée. 
    Si il n'y a plus de points en attente dans le fichier `point.txt`, alors la consigne sera la position actuelle du robot.
    """

    def __init__(self, distance_tolerance, angle_tolerance, maxLinVelStopped, maxAngVelStopped, fichier):
        """Paramètres pour initialiser la classe :

        Args:
            distance_tolerance (float): distance de tolérance pour affirmer que la cible est atteinte.
            angle_tolerance (float): angle de tolérance pour affirmer que le robot est bien positionner.
            maxLinVelStopped (float): Seuil de tolérance pour définir une vitesse linéaire comme nulle, parametrée dans le ROSlaunch.
            maxAngVelStopped (float): Seuil de tolérance pour définir une vitesse angulaire comme nulle, parametrée dans le ROSlaunch.
            fichier (char): Nom du fichier contenant les points.
        """
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
        """Fonction qui met à jour la position actuelle du robot dans la classe.

        Args:
            robotPose (Pose): Position actuelle su robot.
        """
        self.robotPose = robotPose


    def send_new_consign(self):
        """Fonction qui met à jour la nouvelle consigne que doit suivre le robot.

        Returns:
            Pose2D: La nouvelle consigne.
        """
        if isPosition_reached(self.robotPose, self.robotConsign, self.distance_tolerance):
            self.update_robot_consign()
        
        return self.robotConsign


    def update_robot_consign(self):
        """Fonction qui génère la nouvelle consigne du robot en fonction de point dans le fichier `points.txt`. 
        Lorsque tous les points ont été lu, la consigne devient la postion actuelle du robot. (Cela permet de l'immobiliser).
        """
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
        """Fonction pour lire le fichier .txt contenant les points de consigne du robot.

        Args:
            nomFichier (char): nom du fichier
        """
        fichier = open(nomFichier, "r")

        line = fichier.readline()
        while line != "":
            self.listCoord.append([float(x) for x in line.split(" ")])
            line = fichier.readline()

        print(self.listCoord)
        fichier.close()
