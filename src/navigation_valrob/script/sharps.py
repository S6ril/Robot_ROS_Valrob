# coding: utf-8
# @author S6ril

"""
Cette classe permet de gérer la communication avec les Sharps sur une carte arduino annexe.

"""

from sensor_msgs.msg import Range
import serial
import time


class Sharps(object):


    def __init__(self, portserial, bauderate, nbSharps):
        """Initialisation des variables internes de la classe.

        Args:
            portserial (char): Port USB de l'arduino
            bauderate (float): bauderate de la carte
        """
        super(Sharps, self).__init__()
        self.range = Range()
        self.rangeSharps = [0] *nbSharps

        self.serial = serial.Serial()
        self.serial.port = portserial
        self.serial.baudrate = bauderate
        self.serial.timeout = 0
        self.serial.open()


    def __del__(self):
        """
        Destructeur de la classe.
        Permet de fermer le port Serial.
        """
        self.serial.close()
        print("serial close")

    def cleanSerial(self):
        """
        Nettoyage du buffer pour éviter une saturation.
        On appelle cette fonction après chaques commandes Gcode executées.
        """
        self.serial.flushInput()
        self.serial.flushOutput()

    def get_range(self):
        if (self.serial.is_open):
            message = self.serial.readlines()  # Lecture du port serial

            # print("message =", message)
            if (len(message) > 0):
                message = message[0].decode()  # Conversion bytes en str
                message = message.rstrip()  # Enlève \n
                message = message.split(", ")  # Conversion str en list

                # print(message)
                self.rangeSharps[int(message[0])] = int(message[1])

                print(self.rangeSharps)
                # # Répartition des valeurs dans la variable position.
                # self.robotPose.x = float(message[1])
                # self.robotPose.y = float(message[3])
                # self.robotPose.theta = float(message[5])

            self.cleanSerial()
        # return self.robotPose





if __name__ == "__main__":
    sharp = Sharps("/dev/ttyUSB0", 9600, 4)

    try:
        while True:
            sharp.get_range()
            time.sleep(0.5)
    except KeyboardInterrupt:
        sharp.__del__()
