#ifndef DEF_CONTROL
#define DEF_CONTROL

#include <math.h>
#include "Config.h"
#include "type.h"
#import <Arduino.h>

class Control
{
public :

    /**
    Permet d'inverser le sens de rotation
     */
    bool inverte = true;


    /**
    * Mise en place des paramètres des moteurs pour la classe.
    */
    void setup(motorParam motorL, motorParam motorR);


    void setMotorSpeed(int speed, motorParam motor);

    void stop(motorParam motorL, motorParam motorR);

    
    motorParam m_motorLParam;
    motorParam m_motorRParam;

};



#endif
