#!/usr/bin/python3
import sys
import usb.core
import usb.util
from math import atan2
import time



class MouseData(object):
    """Classe pour stocker les datas de la mouse
    """
    def __init__(self):
        super(MouseData, self).__init__()
        self.x = 0
        self.y = 0

class Odometer(object):
    """Classe pour mesurer une distance avec une souris d'ordinateur.
    """
    def __init__(self, IDVendor, IDProduct):
        """Pour obtenir les ID de la souris, sous linux :
        - lsusb
        à partir de là on identifie la souris, dans mon cas : "Bus 001 Device 016: ID 046d:c05a Logitech, Inc. M90/M100 Optical Mouse"
        IDVendor : 0x+ 046d
        IDProcduct : 0x+ c05a
        
        Puis avant de lancer le programme, on donne les droits de lecture et d'écriture sur la souris :
        - sudo chmod a+rw /dev/bus/usb/001/016
        Permet de capter les déplacements de la souris

        :param IDVendor: identificateur unique de la souris
        :type IDVendor: int
        :param IDProduct: identificateur unique de la souris
        :type IDProduct: int
        """
        super(Odometer, self).__init__()
        self.dev = usb.core.find(idVendor=IDVendor, idProduct=IDProduct)
        self.interface = 0
        self.endpoint = self.dev[0][(0, 0)][0]
        self.data = 0
        
        self.robotData = MouseData()
        self.robotPose = MouseData()



        if self.dev.is_kernel_driver_active(self.interface) is True:
            # tell the kernel to detach
            self.dev.detach_kernel_driver(self.interface)
            # claim the device
            usb.util.claim_interface(self.dev, self.interface)

    
    def read_mouse(self):
        try:
            # Lorsque l'on dirige la souris vers le haut, Y de-croissant !!
            self.data = self.dev.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize)
            self.robotData.x = self.data[1]
            self.robotData.y = self.data[2]
        
        except usb.core.USBError as e:
            # self.data = None
            self.robotData.x = 0
            self.robotData.y = 0

            if e.args == ('Operation timed out',):
                print("ERROR")



    def determine_position(self):
        
        self.read_mouse()

        if self.robotData.x >= 129:
            self.robotData.x = -(~self.robotData.x & 0xFF)

        if self.robotData.y >= 129:
            self.robotData.y = -(~self.robotData.y & 0xFF)
        
        self.robotPose.x += self.robotData.x
        self.robotPose.y -= self.robotData.y #Changement de signe pour un affichage matplotlib ensuite
        

        draw(self.robotPose.x, self.robotPose.y)





    

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    def draw(x, y):
        plt.scatter(x, y)
        plt.show()
        plt.pause(0.0001)

    odometer = Odometer(0x046d, 0xc05a)

    plt.ion()
    fig = plt.figure()



    while True:
        try:
            #odometer.read_mouse()
            #print("mouse =", odometer.robotData.__dict__)

            # draw(odometer.robotSpeed.linear.x, odometer.robotSpeed.linear.y)

            odometer.determine_position()
            print(odometer.robotPose.__dict__)

        except KeyboardInterrupt:
            break



