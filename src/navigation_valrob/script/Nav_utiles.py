# coding: utf-8

# @author S6ril & Starfunx


"""
Le but de cette librairie est de fournir des fonctions générales pour le déplacement d'un robot.

"""

from math import sqrt, pow, atan2, pi


def rotation(posRobot, posCible):
    """Fonction pour gerer la rotation du robot

    @param posRobot: Position actuelle du robot
    :type posRobot: Pose()
    @param posCible: Positio de la cible
    :type posCible: Pose2D()
    @return: Angle de rotation
    :rtype: float
    """
    deltax = posCible.x - posRobot.x
    deltay = posCible.y - posRobot.y
    return atan2(deltay , deltax) - posRobot.theta


def distance_euclidienne(posRobot, posCible):
    """Fonction pour calculer la distance euclidienne

    :param posRobot: Position du robot
    :type posRobot: Pose()
    :param posCible: Position de la consignz
    :type posCible: Pose2D()
    :return: Distance euclidienne entre la postion du robot et la consigne
    :rtype: float
    """
    deltax = posCible.x - posRobot.x
    deltay = posCible.y - posRobot.y
    return sqrt( pow( deltax, 2) + pow( deltay, 2) )

def reduction_angle(angle):
    """Fontion pour remettre l'angle dans entre [-Pi/2, Pi/2]

    :param angle: angle en radian à réduire
    :type angle: float
    :return: angle en radian réduit
    :rtype: float
    """
    while angle > pi/2:
        angle -= 2*pi
    while -pi/2 > angle:
        angle += 2*pi

    return angle

def isStopped(commandVel, maxLinVelStopped, maxAngVelStopped):
    """Fonction pour vérifier si le robot est bien stoppé.

    :param commandVel: la commande du robot en vitesse
    :type commandVel: Twist()
    :param maxLinVelStopped: Seuil de tolérance pour définir une vitesse linéaire comme nulle, parametrée dans le ROSlaunch.
    :type maxLinVelStopped: float
    :param maxAngVelStopped: Seuil de tolérance pour définir une vitesse angulaire comme nulle, parametrée dans le ROSlaunch.
    :type maxAngVelStopped: float
    :return: Vrai ou Faux
    :rtype: Booleen
    """
    if (sqrt(commandVel.linear.x*commandVel.linear.x + commandVel.linear.y*commandVel.linear.y + commandVel.linear.z*commandVel.linear.z)  < maxLinVelStopped):
        if (sqrt(commandVel.angular.x*commandVel.angular.x + commandVel.angular.y*commandVel.angular.y + commandVel.angular.z*commandVel.angular.z)  < maxAngVelStopped):
            return True

    return False


def isPosition_reached(pose, poseConsign, distance_tolerance):
    """Fonction pour vérifier si la position souhaitée est bien atteinte.

    :param pose: Position actuelle du robot.
    :type pose: Pose()
    :param poseConsign: Position de la consigne du robot.
    :type poseConsign: Pose2D()
    :param distance_tolerance: seuil de tolérance pour accepter que le robot est bien à la position désirée, parametrée dans le ROSlaunch
    :type distance_tolerance: float
    :return: Vrai ou Faux
    :rtype: Booleen
    """
    if abs(poseConsign.x - pose.x) < distance_tolerance and abs(poseConsign.y - pose.y) < distance_tolerance:
        return True

    return False


def isGoal_reached(robotPose, robotConsign, distance_tolerance, commandVel, maxLinVelStopped, maxAngVelStopped):
    """Fonction pour vérifier que le robot a bien atteint l'objectif désiré.

    :param robotPose: Position actuelle du robot.
    :type robotPose: Pose()
    :param robotConsign: Position de la consigne du robot.
    :type robotConsign: Pose2D()
    :param distance_tolerance: seuil de tolérance pour accepter que le robot est bien à la position désirée, parametrée dans le ROSlaunch
    :type distance_tolerance: float
    :param commandVel: la commande du robot en vitesse
    :type commandVel: Twist()
    :param maxLinVelStopped: Seuil de tolérance pour définir une vitesse linéaire comme nulle, parametrée dans le ROSlaunch.
    :type maxLinVelStopped: float
    :param maxAngVelStopped: Seuil de tolérance pour définir une vitesse angulaire comme nulle, parametrée dans le ROSlaunch.
    :type maxAngVelStopped: float
    :return: Vrai ou Faux
    :rtype: Booleen
    """
    #x, y, angle
    if isPosition_reached(robotPose,
                          robotConsign,
                          distance_tolerance):

        if (isStopped(commandVel,
                    maxLinVelStopped,
                    maxAngVelStopped) ):
            return True

    return False
