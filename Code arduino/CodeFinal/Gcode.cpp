#include "Gcode.h"


void Gcode::DecompoGcode(String commande)
/**
 * @brief Fonction qui va extraire du char transmis en série les différentes commandes (et leurs valeurs associés)
 * 
 */
{
    if (commande != "\0")
    {
        // Serial.println(commande);
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
        // Serial.println(commande.substring(c - char_int-1).toInt());
        Compare(letter, commande.substring(c - char_int-1).toInt() ); // Appel de la fonction pour la dernière commande.
    }


}









void Gcode::Compare(int lettre, float value)
{
    switch (lettre) 
    {
    case 'A':
        m_A = value;
        param += 512;
        break;

    case 'B':
        m_B = value;
        param += 1024;
        break;

    case 'C':
        m_C = value;
        param += 2048;
        break;

    case 'D':
        m_D = value;
        param += 4096;
        break;

    case 'E':
        m_E = value;
        param += 8192;
        break;

    case 'F':
        m_F = value;
        param += 16384;
        break;

    case 'G':
        m_G = value;
        param += 1;
        break;

    case 'H':
        m_H = value;
        param += 32768;
        break;

    case 'I':
        m_I = value;
        param += 65536;
        break;

    case 'J':
        m_J = value;
        param += 131072;
        break;

    case 'K':
        m_K = value;
        param += 262144;
        break;

    case 'L':
        m_L = value;
        param += 524288;
        break;

    case 'M':
        m_M = value;
        param += 2;
        break;

    case 'N':
        m_N = value;
        param += 4;
        break;

    case 'O':
        m_O = value;
        param += 1048576;
        break;

    case 'P':
        m_P = value;
        param += 128;
        break;

    case 'Q':
        m_Q = value;
        param += 2097152;
        break;

    case 'R':
        m_R = value;
        param += 4194304;
        break;

    case 'S':
        m_S = value;
        param += 64;
        break;

    case 'T':
        m_T = value;
        param += 256;
        break;

    case 'U':
        m_U = value;
        param += 8388608;
        break;

    case 'V':
        m_V = value;
        param += 16777216;
        break;

    case 'W':
        m_W = value;
        break;
        param += 33554432;

    case 'X':
        m_X = value;
        param += 8;
        break;

    case 'Y':
        m_Y = value;
        param += 16;
        break;

    case 'Z':
        m_Z = value;
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
