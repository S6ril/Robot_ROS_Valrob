# coding: utf-8
"""
@license
@author S6ril & Starfunx
"""

import rospy
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose
from math import sqrt, pow, atan2, cos, sin

from Consigne_point import Consigne_Point



def consigne_Point():
    rospy.init_node('consigne_point', anonymous=True)

    # rospy.Subscriber("/turtle1/pose", Pose, motion_controller.update_robot_pos)
    pub_consigne_pos = rospy.Publisher('/turtle1/consign', Pose2D, queue_size=10)

    distance_tolerance = rospy.get_param('distance_tolerance', 0.5)
    angle_tolerance = rospy.get_param('angle_tolerance', 0.5)
    maxLinVelStopped = rospy.get_param('maxLinVelStopped', 0.5)
    maxAngVelStopped = rospy.get_param('maxAngVelStopped', 0.5)
    consigne_point = Consigne_Point(distance_tolerance, angle_tolerance, maxLinVelStopped, maxAngVelStopped)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub_consigne_pos.publish( consigne_point.update_robot_consign  )
        rate.sleep()



if __name__ == '__main__':
    try:
        consigne_Point()
    except rospy.ROSInterruptException:
        pass
