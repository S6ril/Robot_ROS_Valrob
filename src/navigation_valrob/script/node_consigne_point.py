#!/usr/bin/python3

# @author S6ril & Starfunx


"""
Cette node permet de donner comme consigne de se diriger vers une succession de points définis dans un fichier `.txt`. 

"""


import rospy
from geometry_msgs.msg import Twist, Pose2D

from math import sqrt, pow, atan2, cos, sin
from Nav_utiles import isPosition_reached

from Consigne_point import Consigne_Point


def consigne_Point():
    """
    Fonction principale pour la node de la gestion de la consigne.
    Elle demande des valeurs définies dans le roslaunch :
        - distance_tolerance
        - angle_tolerance
        - maxLinVelStopped
        - maxAngVelStopped
    """
    rospy.init_node('consigne_point', anonymous=True)
    distance_tolerance = rospy.get_param('distance_tolerance',0)
    angle_tolerance    = rospy.get_param('angle_tolerance', 0)
    maxLinVelStopped   = rospy.get_param('maxLinVelStopped', 0)
    maxAngVelStopped   = rospy.get_param('maxAngVelStopped', 0)
    
    Cpoint = Consigne_Point(distance_tolerance, angle_tolerance,
                            maxLinVelStopped, maxAngVelStopped, '/home/cyril/catkin_ws/point.txt')


    pub_consigne_pos = rospy.Publisher('/robot/consign', Pose2D, queue_size=10)
    rospy.Subscriber("/robot/pose", Pose2D, Cpoint.update_robot_pose)

    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown():
        pub_consigne_pos.publish(Cpoint.send_new_consign())
        
        rate.sleep()



if __name__ == '__main__':
    try:
        consigne_Point()
    except rospy.ROSInterruptException:
        pass
