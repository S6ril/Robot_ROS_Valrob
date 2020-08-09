#include "SharpIR.h"

#define MODELE GP2Y0A41SK0F


const int nombreSharp = 4;
uint8_t pin[nombreSharp] = {A0, A1, A2, A3};

SharpIR sharp[nombreSharp];


void setup()
{
  Serial.begin( 9600 ); //Enable the serial comunication
  int i;
  for (i=0; i< nombreSharp; i++)
  {
      sharp[i] = SharpIR( SharpIR::MODELE, pin[i] );
  }
  // Serial.println("Sharp, distance");
}

int i = 3;
void loop()
{
  int distance = sharp[i].getDistance(); //Calculate the distance in centimeters and store the value in a variable

  Serial.print(i);
  Serial.print(", ");
  Serial.println( distance ); //Print the value to the serial monitor


  i = (i+1) %nombreSharp;
  delay(500);
}
