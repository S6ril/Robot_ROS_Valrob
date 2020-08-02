# class Coordo:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.z = 0

# class Twist:
#     def __init__(self):
#         self.linear  = Coordo()
#         self.angular = Coordo()

from geometry_msgs.msg import Twist




class Joystick_driver(object):
    """docstring for Joystick_driver."""

    def __init__(self):
        super(Joystick_driver, self).__init__()
        self.axes = [0, 0, 0, 0]
        self.buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.twist = Twist()

        self.scale = 50


    def update_command_joy(self, joy):
        self.axes = joy.axes
        self.buttons = joy.buttons


    def update_command_vel(self):
        self.twist.angular.z = self.axes[0] *self.scale
        self.twist.linear.x = self.buttons[0] - self.buttons[1]

        return self.twist
