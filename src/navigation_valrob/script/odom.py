#!/usr/bin/python3
import sys
import usb.core
import usb.util
from math import atan2

from geometry_msgs.msg import Pose2D


def toNegative(value):
    if value > 127:
        value = value - 255
    
    return value

class Odometer(object):
    
    def __init__(self, IDVendor, IDProduct):
        super(Odometer, self).__init__()
        self.dev = usb.core.find(idVendor=IDVendor, idProduct=IDProduct)
        self.interface = 0
        self.endpoint = self.dev[0][(0, 0)][0]
        self.data = 0
        
        self.robotPose = Pose2D()

        if self.dev.is_kernel_driver_active(self.interface) is True:
            # tell the kernel to detach
            self.dev.detach_kernel_driver(self.interface)
            # claim the device
            usb.util.claim_interface(self.dev, self.interface)

    
    def read_speed(self):
        try:
            # Lorsque l'on dirige la souris vers le haut, Y de-croissant !!
            self.data = self.dev.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize)
            self.robotPose.x = toNegative(self.data[1])
            self.robotPose.y = toNegative(self.data[2])

            self.robotPose.theta = atan2(self.robotPose.x, 15)
        
        except usb.core.USBError as e:
            self.data = None
            self.robotPose.x = 0
            self.robotPose.y = 0
            self.robotPose.theta = 0
            if e.args == ('Operation timed out',):
                print("ERROR")





    
    def __del__(self):
        usb.util.release_interface(self.dev, self.interface)
        # reattach the device to the OS kernel
        self.dev.attach_kernel_driver(self.interface)




    

if __name__ == "__main__":
    odometer = Odometer(0x046d, 0xc018)


    while True:
        try:
            odometer.read_speed()
            print("speed X =",odometer.robotPose)
        
        except KeyboardInterrupt:
            break



