#include "Gcode.h"




// void Gcode::DecompoGcode(String commande){
//   // Serial.print(commande);

//   int c = 0; //Incrément de la boucle principale
//   int sub_c = 0; //Incrément pour le substring (petite tranche de la liste)
//   int tString = 190; //Taille max du string
//   param=0;

//   for (c=0; c < tString; c++){
//     //On parcourt le string carractère par carractère

//     if ( isDigit(commande[c]) || isPunct(commande[c]) ){
//       //Increment pour determiner la taille du sub string contenant les nombres
//       sub_c++;
//     }
//     else {
//       //Ici on a la position d'un nombre, on lui associe alors la lettre correspondantes.
//       //On assigne les variables (ABCD...) avec la fonction compare.
//       //Pour la propreté du code, la comparaison se fait dans un autre fichier.
//       // 
//       Compare(commande, commande[c-sub_c-1], c, sub_c );

//       sub_c = 0; //remise à zero du sub string
//     }

//   }
// }


void Gcode::DecompoGcode(String commande)
{
  if (commande != '\0')
  {
    commande.replace(" ", ""); //Delete all space : no need

    char letter = commande[0]; //Première commande
    int char_int = 0; //  incrément pour définir la valeur de la commande
    int c;
    
    for (c =1; commande[c] != '\0'; c++)
    /**
     * @brief On parcourt la liste de carractère.
     * Dans un premier temps on sauvegarde la lettre, 
     * puis au prochain carractère, on connait la valeur associé à la lettre initiale
     */
    {

      if (isAlpha(commande[c]) )
      {
        Compare(letter, commande.substring(c-char_int, c).toInt() );
        letter = commande[c]; // Commande suivante
        char_int = 0; //RaZ
      }
      else if ( isDigit(commande[c]) )
      {
        char_int++;
      }

    }
    Compare(letter, commande.substring(c - char_int-1).toInt() ); // Appel de la fonction pour la dernière commande.
  }
  

}









void Gcode::Compare(int lettre, float value){
  Serial.println("Ici");
  Serial.println(lettre);
  Serial.println(value);
  
  
  switch (lettre) {
    int sub_c = 0;

    case 'A':
      m_A = value;
      if (sub_c > 0)
            param += 512;
      break;

    case 'B':
      m_B = value;
      if (sub_c > 0)
        param += 1024;
      break;

    case 'C':
      m_C = value;
      if (sub_c > 0)
        param += 2048;
      break;

    case 'D':
      m_D = value;
      if (sub_c > 0)
        param += 4096;
      break;

    case 'E':
    m_E = value;
    if (sub_c > 0)
      param += 8192;
    break;

    case 'F':
    m_F = value;
    if (sub_c > 0)
      param += 16384;
    break;

    case 'G':
    m_G = value;
    if (sub_c > 0)
      param += 1;
    break;

    case 'H':
    m_H = value;
    if (sub_c > 0)
      param += 32768;
    break;

    case 'I':
    m_I = value;
    if (sub_c > 0)
      param += 65536;
    break;

    case 'J':
    m_J = value;
    if (sub_c > 0)
      param += 131072;
    break;

    case 'K':
    m_K = value;
    if (sub_c > 0)
      param += 262144;
    break;

    case 'L':
    m_L = value;
    if (sub_c > 0)
      param += 524288;
    break;

    case 'M':
    m_M = value;
    if (sub_c > 0)
      param += 2;
    break;

    case 'N':
    m_N = value;
    if (sub_c > 0)
      param += 4;
    break;

    case 'O':
    m_O = value;
    if (sub_c > 0)
      param += 1048576;
    break;

    case 'P':
    m_P = value;
    if (sub_c > 0)
      param += 128;
    break;

    case 'Q':
    m_Q = value;
    if (sub_c > 0)
      param += 2097152;
    break;

    case 'R':
    m_R = value;
    if (sub_c > 0)
      param += 4194304;
    break;

    case 'S':
    m_S = value;
    if (sub_c > 0)
      param += 64;
    break;

    case 'T':
    m_T = value;
    if (sub_c > 0)
      param += 256;
    break;

    case 'U':
    m_U = value;
    if (sub_c > 0)
      param += 8388608;
    break;

    case 'V':
    m_V = value;
    if (sub_c > 0)
      param += 16777216;
    break;

    case 'W':
    m_W = value;
    if (sub_c > 0)
    break;
      param += 33554432;

    case 'X':
    m_X = value;
    if (sub_c > 0)
      param += 8;
    break;

    case 'Y':
    m_Y = value;
    if (sub_c > 0)
      param += 16;
    break;

    case 'Z':
    m_Z = value;
    if (sub_c > 0)
      param += 32;
    break;

  }


}


void Gcode::affiche()
{

  Serial.print("Traduction =\n");

  Serial.print("m_A = \t");
  Serial.println(m_A);

  Serial.print("m_B = \t");
  Serial.println(m_B);

  Serial.print("m_C = \t");
  Serial.println(m_C);

  Serial.print("m_D = \t");
  Serial.println(m_D);

  Serial.print("m_E = \t");
  Serial.println(m_E);

  Serial.print("m_F = \t");
  Serial.println(m_F);

  Serial.print("m_G = \t");
  Serial.println(m_G);

  Serial.print("m_H = \t");
  Serial.println(m_H);

  Serial.print("m_I = \t");
  Serial.println(m_I);

  Serial.print("m_J = \t");
  Serial.println(m_J);

  Serial.print("m_K = \t");
  Serial.println(m_K);

  Serial.print("m_L = \t");
  Serial.println(m_L);

  Serial.print("m_M = \t");
  Serial.println(m_M);

  Serial.print("m_N = \t");
  Serial.println(m_N);

  Serial.print("m_O = \t");
  Serial.println(m_O);

  Serial.print("m_P = \t");
  Serial.println(m_P);

  Serial.print("m_Q = \t");
  Serial.println(m_Q);

  Serial.print("m_R = \t");
  Serial.println(m_R);

  Serial.print("m_S = \t");
  Serial.println(m_S);

  Serial.print("m_T = \t");
  Serial.println(m_T);

  Serial.print("m_U = \t");
  Serial.println(m_U);

  Serial.print("m_V = \t");
  Serial.println(m_V);

  Serial.print("m_W = \t");
  Serial.println(m_W);

  Serial.print("m_X = \t");
  Serial.println(m_X);

  Serial.print("m_Y = \t");
  Serial.println(m_Y);

  Serial.print("m_Z = \t");
  Serial.println(m_Z);
}
