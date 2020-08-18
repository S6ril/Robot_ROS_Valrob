# coding: utf-8
# @author S6ril

"""
Cette classe permet de gérer la communication avec les Sharps sur une carte arduino annexe.

"""

from navigation_valrob.msg import Sharps

import serial
import time


class Class_Sharps(object):
    """Classe permettant de récupérer la distance donnée par plusieurs Sharps.

    NB: Cette classe s'appelle `Class_` pour ne pas être confondue avec le message Sharps()
    """

    def __init__(self, portserial, bauderate, nbSharps):
        """Initialisation des variables internes de la classe.

        Args:
            portserial (char): Port USB de l'arduino
            bauderate (float): bauderate de la carte
            nbSharps    (int): nombre de sharps connecté à la carte.
        """
        self.sharps = Sharps()
        self.sharps.ranges = [0] *nbSharps

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
        """Fonction pour récupérer les distances données par les sharps sur le port série de la carte

        Returns:
            Sharps: message custom du paquet navigation_valrob qui regroupe une liste avec toutes les mesures des Sharps.
        """
        if (self.serial.is_open and self.serial.inWaiting()> 0):
            # Verification que serial est ouvert et qu'il y a quelque chose à lire.
            message = self.serial.readlines()  # Lecture du port serial

            # print("message =", message)
            if (len(message) > 0):
                message = message[0].decode()  # Conversion bytes en str
                message = message.rstrip()  # Enlève \n
                message = message.split(", ")  # Conversion str en list

                # Affectation au message.
                self.sharps.ranges[int(message[0])] = int(message[1])

            self.cleanSerial()
        return self.sharps





if __name__ == "__main__":
    sharp = Class_Sharps("/dev/ttyUSB0", 9600, 4)

    try:
        while True:
            print(sharp.get_range())
            
    except KeyboardInterrupt:
        sharp.__del__()
