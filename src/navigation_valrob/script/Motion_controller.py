# coding: utf-8

# @author S6ril & Starfunx


from math import sqrt, pow, atan2, cos, sin, pi

try:
    """Importation des variables ROS
    """
    from geometry_msgs.msg import Twist, Pose2D

except ImportError:
    """Si ROS n'est pas dans le système on crée les classes.
    Cela permet d'utiliser cette classe sans ROS
    """
    class Pose2D():
        x = 0
        y = 0
        theta = 0

    class coord():
        x = 0
        y = 0
        z = 0

    class Twist():
        linear = coord()
        angular = coord()


from Nav_utiles import distance_euclidienne, rotation, reduction_angle


class Motion_controller(object):
    """Cette classe permet de gérer les déplacements du robot, afin qu'il se dirige vers la consigne donnée."""

    def __init__(self, krho, kalpha):
        super(Motion_controller, self).__init__()
        self.krho = float(krho)
        self.kalpha = float(kalpha)
        self.commandVel = Twist()
        self.robotPose = Pose2D()
        self.robotConsign = Pose2D()
        self.initialise = True
        self.robotPoseInitiale = Pose2D()



    def update_command_vel(self):
        """Fonction qui met à jour la commande du robot dès qu'elle est appelée.

        Returns:
            Twist: La commande en vitesse et vitesse angulaire
        """
        rho = distance_euclidienne(self.robotPose, self.robotConsign)

        alpha = rotation(self.robotPose, self.robotConsign)
        alpha = reduction_angle(alpha)

        commandVel = Twist()
        commandVel.linear.x = self.krho*rho*cos(alpha)
        commandVel.angular.z = self.kalpha*alpha

        return commandVel

    def update_robot_pos(self, robotPose):
        """Fonction qui met à jour la position du robot dès qu'elle est appelée.

        Args:
            robotPose (Pose2D): Position actuelle du robot
        """
        self.robotPose = robotPose
        if self.initialise:
            self.robotPoseInitiale = robotPose
            self.robotConsign.x = robotPose.x
            self.robotConsign.y = robotPose.y
            self.initialise = False


    def update_robot_consign(self, robotConsign):
        """Fonction qui met à jour la consigne du robot, dès qu'elle est appelé.

        Args:
            robotConsign (Pose2D): Consigne a donné au robot
        """
        self.robotConsign = robotConsign
