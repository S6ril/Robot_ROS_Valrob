#!/usr/bin/python3
# @author S6ril


"""Cette node permet de gérer la détection d'obstacle.
"""


import rospy
from sensor_msgs.msg import Range



def detection_obstacle():

    # Initiation de la classe


    # Initiation de ROS
    rospy.init_node('detection_obstacle', anonymous=True)


    pub_sensor = rospy.Publisher('/robot/range', Range, queue_size=10)  # Sortie

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # Publication de la sortie à 10Hz
        pub_sensor.publish(  )
        rate.sleep()


if __name__ == '__main__':
    try:
        detection_obstacle()
    except rospy.ROSInterruptException:
        pass
