#include "Commande.h"
#include "Gcode.h"



void Commande::executerGcode(String commande){
  gcode.DecompoGcode(commande); //Décomposition du Gcode dans les différentes variables
  // gcode.affiche();

  // Test de la présence de le lettre M
  // M en premier, car c'est elle qui determine l'arret des moteurs.
  if (gcode.hasM()){
    switch (gcode.m_M){
      case 0:
        // Arret
        break;

      case 1:
        // Commande à définir
        break;

      case 666:
        if (Serial.available() )
        {
          Serial.println("Com OK");   
        }
        break;
    }
  }

  // Test de la présence de G
  else if (gcode.hasG()){
    //Test de la varible G
    switch (gcode.m_G){
      case 20:
      // Commande
      break;

      case 1:
      // Commande à définir
      break;
    }
  }

  // Variable de Test en L
  else if (gcode.hasL())
  {
    switch (int(gcode.m_L)){
      case 0:
      digitalWrite(3, LOW);
      break;

      case 1:
      digitalWrite(3, HIGH);
      break;
    }
  }



}
