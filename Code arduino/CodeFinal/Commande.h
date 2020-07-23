#ifndef COMM_H
#define COMM_H

#include "Gcode.h"
#include "Control_motor.h"

class Commande
{
  public :

  /**
   * Fonction pour executer les commandes en fonction des Gcodes reçus.
   * @param commande : String Gcode complet.
   */
  void executerGcode(String commande);


  private:
    Gcode gcode; // Définition de la variable Gcode qui récupéra les différentes variables du Gcode.
    Control control;
};
#endif
