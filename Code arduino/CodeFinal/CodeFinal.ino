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
    char commandebuffer[200] = {'\0'};

    if (Serial)
    {
        int i = 0;
        delay(100);
        for (i = 0; i < 200; i++)
        {
            commandebuffer[i] = Serial.read();
            if (!isPrintable(commandebuffer[i]) )
            {
                break;
            }
        }
        commandebuffer[i++]='\0';
    }
    commande.executerGcode(commandebuffer);
}
