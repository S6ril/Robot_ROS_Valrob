# coding: utf-8

# @author S6ril & Starfunx


"""
Le but de cette librairie est de fournir des fonctions générales pour le déplacement d'un robot.

"""

from math import sqrt, pow, atan2, pi

def rotation(posRobot, posCible):
    """
    Fonction pour gérer la rotation du robot vers une cible.
    
    Args:
        posRobot (Pose2D): Position actuelle du robot
        posCible (Pose2D): Position de la consigne

    Returns:
        float: Angle de rotation à effectuer pour se diriger vers la consigne.
    """
    deltax = posCible.x - posRobot.x
    deltay = posCible.y - posRobot.y
    return atan2(deltay , deltax) - posRobot.theta


def distance_euclidienne(posRobot, posCible):
    """
    Fonction pour calculer la distance euclidienne entre le robot et une cible.

    Args:
        posRobot (Pose2D): Position du robot
        posCible (Pose2D): Position de la consigne

    Returns:
        float: Distance euclidienne entre la postion du robot et la consigne
    """
    deltax = posCible.x - posRobot.x
    deltay = posCible.y - posRobot.y
    return sqrt( pow( deltax, 2) + pow( deltay, 2) )

def reduction_angle(angle):
    """
    Fontion pour remettre l'angle dans entre [-Pi/2, Pi/2].

    Args:
        angle (flaot): Angle en rad à réduire

    Returns:
        float: Angle en radian réduit
    """
    while angle > pi/2:
        angle -= 2*pi
    while -pi/2 > angle:
        angle += 2*pi

    return angle

def isStopped(commandVel, maxLinVelStopped, maxAngVelStopped):
    """
    Fonction pour vérifier si le robot est bien stoppé.

    Args:
        commandVel (Twist): La commande du robot en vitesse
        maxLinVelStopped (float): Seuil de tolérance pour la vitesse linéaire
        maxAngVelStopped (float): Seuil de tolérance pour la vitesse angulaire

    Returns:
        Booleen
    """
    if (sqrt(commandVel.linear.x*commandVel.linear.x + commandVel.linear.y*commandVel.linear.y + commandVel.linear.z*commandVel.linear.z)  < maxLinVelStopped):
        if (sqrt(commandVel.angular.x*commandVel.angular.x + commandVel.angular.y*commandVel.angular.y + commandVel.angular.z*commandVel.angular.z)  < maxAngVelStopped):
            return True

    return False


def isPosition_reached(pose, poseConsign, distance_tolerance):
    """
    Fonction pour vérifier si la position souhaitée est bien atteinte.

    Args:
        pose (Pose): Position actuelle du robot
        poseConsign (Pose2D): Consigne de position
        distance_tolerance (float): Seuil de tolérance pour accepter que le robot à atteint l'objectif

    Returns:
        Booleen
    """
    if abs(poseConsign.x - pose.x) < distance_tolerance and abs(poseConsign.y - pose.y) < distance_tolerance:
        return True

    return False


def isGoal_reached(robotPose, robotConsign, distance_tolerance, commandVel, maxLinVelStopped, maxAngVelStopped):
    """
    Fonction pour vérifier que le robot a bien atteint l'objectif désiré.

    Args:
        robotPose(Pose): Position actuelle du robot.
        robotConsign(Pose2D): Position de la consigne du robot.
        distance_tolerance(float): seuil de tolérance pour accepter que le robot est bien à la position désirée, parametrée dans le ROSlaunch
        commandVel(Twist): la commande du robot en vitesse
        maxLinVelStopped(float): Seuil de tolérance pour définir une vitesse linéaire comme nulle, parametrée dans le ROSlaunch.
        maxAngVelStopped(float): Seuil de tolérance pour définir une vitesse angulaire comme nulle, parametrée dans le ROSlaunch.

    Returns:
        Booleen
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
