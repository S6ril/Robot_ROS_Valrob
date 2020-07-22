#include "Gcode.h"
#include "Commande.h"


Commande commande;
//Creation de l'objet pour traduire le Gcode



void setup() {
    Serial.begin(9600); // open the serial port at 9600 bps:
    Serial.flush();

    //Test Led
    pinMode(3, OUTPUT);
}

void loop() 
{
    int i=0;
    char commandebuffer[200] = {'\0'};

    if (Serial.available())
    {
        delay(100);
        while (Serial.available() && i<200)
        {
            commandebuffer[i++] = Serial.read();
        }
    commandebuffer[i++]='\0';
    }
    commande.executerGcode(commandebuffer);
}
