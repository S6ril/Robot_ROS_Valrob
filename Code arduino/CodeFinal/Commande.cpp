#include "Commande.h"



void Commande::executerGcode(String commande)
/**
 * @brief Fonction qui permet d'exécuter les commandes demandées.
 * 
 */
{
    gcode.DecompoGcode(commande); //Décomposition du Gcode dans les différentes variables
    // gcode.affiche();

    // Test de la présence de le lettre M
    // M en premier, car c'est elle qui determine l'arret des moteurs.
    if (gcode.hasM())
    {
        switch (gcode.m_M)
        {
        case 0:
            // Commande à définir
            Serial.println("J'ai reçu M0");
            break;

        case 1:
            // Commande à définir
            break;


        case 18:
            Serial.println("Stop Motor");
            control.stop(m_motorLParam, m_motorRParam);

            //RaZ des vitesses !!
            gcode.m_I = 0;
            gcode.m_J = 0;
            break;
        
        case 114:
            Serial.print("cons ");
            Serial.print(gcode.m_I);
            break;

        case 115:
            Serial.print("cons ");
            Serial.print(gcode.m_J);
            break;

        case 666:
            Serial.println("Com OK");
            control.setup(m_motorLParam, m_motorRParam);
            Serial.println("Initialisation OK"); 
            break;
        }
    }

    // Test de la présence de G
    else if (gcode.hasG())
    {
        //Test de la varible G
        switch (gcode.m_G)
        {
        case 11:
            Serial.println("Mise en route des moteurs");
            control.setMotorSpeed(gcode.m_I, m_motorLParam);
            control.setMotorSpeed(gcode.m_J, m_motorRParam);
            break;
        
        case 20:
            Serial.println("G20");
            break;
        }
    }

    // Variable de Test en L
    else if (gcode.hasL())
    {
        switch (int(gcode.m_L))
        {
        case 0:
            digitalWrite(3, LOW);
            break;

        case 1:
            digitalWrite(3, HIGH);
            break;
        }
    }

    // Raz des gcode.has()
    gcode.param = 0;
}
