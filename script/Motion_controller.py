# coding: utf-8
"""
@license
@author S6ril & Starfunx
"""

from math import sqrt, pow, atan2, cos, sin, pi
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

from Nav_utiles import distance_euclidienne, rotation, reduction_angle


class Motion_controller(object):
    """docstring for Motion_controller."""

    def __init__(self, krho, kalpha):
        super(Motion_controller, self).__init__()
        self.krho = float(krho)
        self.kalpha = float(kalpha)
        self.commandVel = Twist()
        self.robotPose = Pose()
        self.robotConsign = Pose2D()
        self.initialise = True
        self.robotPoseInitiale = Pose()



    def update_command_vel(self):
        rho = distance_euclidienne(self.robotPose, self.robotConsign)

        alpha = rotation(self.robotPose, self.robotConsign)
        alpha = reduction_angle(alpha)

        commandVel = Twist()
        commandVel.linear.x = self.krho*rho*cos(alpha)
        commandVel.angular.z = self.kalpha*alpha

        return commandVel

    def update_robot_pos(self, robotPose):
        #robot_pos est un tutlesim/Pose
        self.robotPose = robotPose
        if self.initialise:
            self.robotPoseInitiale = robotPose
            self.robotConsign.x = robotPose.x
            self.robotConsign.y = robotPose.y
            self.initialise = False


    def update_robot_consign(self, robotConsign):
        #robot_consign est un geometry_msgs/Pose2D
        self.robotConsign = robotConsign
