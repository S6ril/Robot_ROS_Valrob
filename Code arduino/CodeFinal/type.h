/**
 * @brief Définition des moteurs.
 * Ici on est basé sur des MCC, avec un pont en H comme driver moteur.
 */
typedef struct motorParam motorParam;
 struct motorParam{
    int EnablePin;
    //Pin du sens de rotation
    int Lpin;
    int Rpin;
} ;

//Structure pour les coordonnées.
typedef struct Point Point;
struct Point {
    float x;
    float y;
};
