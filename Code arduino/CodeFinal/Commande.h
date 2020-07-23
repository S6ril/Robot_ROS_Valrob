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

    motorParam m_motorLParam = control.m_motorLParam;
    motorParam m_motorRParam = control.m_motorRParam;
};
#endif
