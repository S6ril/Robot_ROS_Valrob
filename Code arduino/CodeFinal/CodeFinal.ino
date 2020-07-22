#include "Gcode.h"
#include "Commande.h"


String message;


Commande commande;
//Creation de l'objet pour traduire le Gcode



void setup() {
  Serial.begin(9600); // open the serial port at 9600 bps:
  Serial.flush();

  //Test Led
  pinMode(3, OUTPUT);
}

void loop() {


  int i=0;
  char commandebuffer[200] = {'\0'};

  if (Serial.available())  {
      delay(100);
      while (Serial.available() && i<99){
          commandebuffer[i++] = Serial.read();
      }
    commandebuffer[i++]='\0';
    }
    //Serial.print("Message =");
    //Serial.println(message);
    commande.executerGcode(commandebuffer);



}
