#include "Control_motor.h"


/*Setup les moteurs
 */
void Control::setup(motorParam motorLParam, motorParam motorRParam)
{ //setup les moteurs
    m_motorLParam = motorLParam;
    m_motorRParam = motorRParam;

    pinMode(m_motorLParam.EnablePin, OUTPUT);
    pinMode(m_motorRParam.EnablePin, OUTPUT);

    digitalWrite(m_motorLParam.EnablePin, LOW);
    digitalWrite(m_motorRParam.EnablePin, LOW);

}

void Control::setMotorSpeed(int speed, motorParam motor)
{
    digitalWrite(motor.Lpin, HIGH);
    digitalWrite(motor.Rpin, LOW);
    // set speed to 150 out 255
    analogWrite(motor.EnablePin, speed);
}

void Control::stop(motorParam motorL, motorParam motorR)
{
    digitalWrite(motorL.Lpin, LOW);
    digitalWrite(motorL.Rpin, LOW);
    digitalWrite(motorL.EnablePin, LOW);

    digitalWrite(motorR.Lpin, LOW);
    digitalWrite(motorR.Rpin, LOW);
    digitalWrite(motorR.EnablePin, LOW);
}

