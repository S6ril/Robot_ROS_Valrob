#ifndef GCODE_H
#define GCODE_H

#include <Arduino.h>




class Gcode
/**
 * \brief
 * Gcode library for ARDUINO
 * \brief
 * Classe qui permet de dispatcher le Gcode reçu dans différentes variables.
 * Ainsi on connait la valeur de la variable, mais aussi si elle a été reçu lors du dernier appel.
 * (On ne réinitialise pas les valeurs à chaques exécutions)
 *
 * \author S6ril
 * \date 2019-2020
 */
{
  public :

  /**
   * Fonction pour traduire le Gcode et le décomposer en petits parramétres.
   * Les parramètres reçus restent en mémoire ! (A chaques nouvelles receptions, les variables ne sont pas remise à zero)
   * Les décimaux sont séparés par un POINT (.)
   * @param commande : Gcode en entier de taille 190 octets
   */
  void DecompoGcode(String commande);

  /**
   * Permet de mettre dans les variables m_X les valeurs correspondantes données par le Gcode.
   * On crée un substring à partir de la position du dernier chiffre.
   * On modifie aussi la valeur de param. Cela permet ensuite de determiner les valeurs contenus dans le Gcode reçu.
   * On utilise un système de masque (2^n), mais on ne l'affichage pas en en bits.
   * @param stringcomplet Le Gcode complet où l'on va extraire les valeurs
   * @param lettre        La lettre dont l'on veut extraire la valeur
   * @param c             Position du dernier chiffre à extraire
   * @param sub_c         Nombre de chiffres à extraires
   */
  void Compare(int lettre, float value);

  /* Visualisation des différentes variavles.
   * Attention l'affichage print() n'imprime que 2 décimales.
   */
  void affiche();


  //Assignation des différentes variables utiles lors du Gcode
  unsigned int m_G;
  unsigned int m_M;
  unsigned int m_N;

  //Les positions
  float m_X;
  float m_Y;
  float m_Z;

  long m_S;
  long m_P;

  int m_T;

  float m_A;
  float m_B;
  float m_C;
  float m_D;
  float m_E;
  float m_F;
  float m_H;
  float m_I;
  float m_J;
  float m_K;
  float m_L;
  float m_O;
  float m_Q;
  float m_R;
  float m_U;
  float m_V;
  float m_W;


/**
 * Permet de comparer avec un masque la présence d'une lettre récemment ajoutée.
 * Cette fonction est indentique pour toutes les lettres.
 * @return un booléen.
 */
  inline bool hasG()
  {
    return ((param & 1)!= 0);
  }
  inline bool hasM()
  {
    return ((param & 2)!= 0);
  }
  inline bool hasN()
  {
    return ((param & 4)!= 0);
  }
  inline bool hasX()
  {
    return ((param & 8)!= 0);
  }
  inline bool hasY()
  {
    return ((param & 16)!= 0);
  }
  inline bool hasZ()
  {
    return ((param & 32)!= 0);
  }
  inline bool hasS()
  {
    return ((param & 64)!= 0);
  }
  inline bool hasP()
  {
    return ((param & 128)!= 0);
  }
  inline bool hasT()
  {
    return ((param & 256)!= 0);
  }
  inline bool hasA()
  {
    return ((param & 512)!= 0);
  }
  inline bool hasB()
  {
    return ((param & 1024)!= 0);
  }
  inline bool hasC()
  {
    return ((param & 2048)!= 0);
  }
  inline bool hasD()
  {
    return ((param & 4096)!= 0);
  }
  inline bool hasE()
  {
    return ((param & 8192)!= 0);
  }
  inline bool hasF()
  {
    return ((param & 16384)!= 0);
  }
  inline bool hasH()
  {
    return ((param & 32768)!= 0);
  }
  inline bool hasI()
  {
    return ((param & 65536)!= 0);
  }
  inline bool hasJ()
  {
    return ((param & 131072)!= 0);
  }
  inline bool hasK()
  {
    return ((param & 262144)!= 0);
  }
  inline bool hasL()
  {
    return ((param & 524288)!= 0);
  }
  inline bool hasO()
  {
    return ((param & 1048576)!= 0);
  }
  inline bool hasQ()
  {
    return ((param & 2097152)!= 0);
  }
  inline bool hasR()
  {
    return ((param & 4194304)!= 0);
  }
  inline bool hasU()
  {
    return ((param & 8388608)!= 0);
  }
  inline bool hasV()
  {
    return ((param & 16777216)!= 0);
  }
  inline bool hasW()
  {
    return ((param & 33554432)!= 0);
  }


  private :
  //Parramètre contenant la masque du Gcode. Il sera testé par la suite.
  unsigned long param = 0;

};
#endif
