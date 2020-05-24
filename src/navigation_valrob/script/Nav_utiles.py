# coding: utf-8
"""
@license
@author S6ril & Starfunx
"""
from math import sqrt, pow, atan2, pi

def rotation(posRobot, posCible):
    deltax = posCible.x - posRobot.x
    deltay = posCible.y - posRobot.y
    return atan2(deltay , deltax) - posRobot.theta

def distance_euclidienne(posRobot, posCible):
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


def isGoal_reached(motion_controller, consigne_point):
    #x, y, angle
    if isPosition_reached(motion_controller.robotPose,
                          motion_controller.robotConsign,
                          consigne_point.distance_tolerance):

                          if (isStopped(motion_controller.commandVel,
                                        consigne_point.maxLinVelStopped,
                                        consigne_point.maxAngVelStopped) ):
                                        return True

    return False
