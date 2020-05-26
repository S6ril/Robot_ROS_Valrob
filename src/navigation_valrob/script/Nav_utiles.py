# coding: utf-8
"""
@license
@author S6ril & Starfunx

@brief : Cette bibliothèque ressence les fonctions qui peuvent être utile pour la gestion des déplacements du robot.
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
    while angle > pi/2:
        angle -= 2*pi
    while -pi/2 > angle:
        angle += 2*pi

    return angle

def isStopped(commandVel, maxLinVelStopped, maxAngVelStopped):
    if (sqrt(commandVel.linear.x*commandVel.linear.x + commandVel.linear.y*commandVel.linear.y + commandVel.linear.z*commandVel.linear.z)  < maxLinVelStopped):
        if (sqrt(commandVel.angular.x*commandVel.angular.x + commandVel.angular.y*commandVel.angular.y + commandVel.angular.z*commandVel.angular.z)  < maxAngVelStopped):
            return True

    return False


def isPosition_reached(pose, poseConsign, distance_tolerance):
    if abs(poseConsign.x - pose.x) < distance_tolerance and abs(poseConsign.y - pose.y) < distance_tolerance:
        return True

    return False


def isGoal_reached(robotPose, robotConsign, distance_tolerance, commandVel, maxLinVelStopped, maxAngVelStopped):
    #x, y, angle
    if isPosition_reached(robotPose,
                          robotConsign,
                          distance_tolerance):

        if (isStopped(commandVel,
                    maxLinVelStopped,
                    maxAngVelStopped) ):
            return True

    return False
