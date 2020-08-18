# Lancement

## Lancement sans ROS

Il est possible d’utiliser le code sans ROS. 

Pour cela ajoutez dans votre dossier de travail (le même où se situe votre script Python) les fichiers suivant :
* `driver_baseRoulante` : Cela permet de controler les moteurs par communication Gcode via le port série.
* `Consigne_point` : permet de lire un fichier de points et d’envoyer une consigne lorsque le point a été atteind. 
* `Motion_controller`
* `Nav_utiles` : outils qui peuvent être utile à la navigation.

Le plus interressant est le `driver_baseRoulante`. Dans votre script Python :

    from driver_BaseRoulante import *

    # Initialisation de la communication
    robot = Communication_Gcode("COM5", 115200)

    # Activation des moteurs
    robot.enable_motors()

    # Déplacement lent vers un point
    robot.set_slow_move_to(x, y, theta)

Avec les différentes fonctions, il sera alors possible de diriger le robot.

``` note:: Le fichiers **nodes** sont utiles pour le langage ROS. Ils permettent de gérer les entrées et les sorties.
```

## Lancement avec ROS

Maintenant que le code est téléchargé et placé dans l’environnement `catkin_ws`. 
On a alors un dossier de la forme :

    catkin_ws
        -- src
        ---- navigation_valrob
        ------ script
        ------ launch

Il faut alors lancer ROS ! Pour cela, j’utilise un [ROSLaunch](https://wiki.ros.org/roslaunch/Commandline%20Tools/) qui me permet de lancer un Roscore et des nodes simultanément.

    cd catkin_ws/
    catkin_make
    source ./devel/setup.bash  

La dernière commande `source` permet « d’apprendre » au terminal toutes les nouvelles commandes contenue dans ce dossier.


### Configuration de l'itinéraire

On configure dans le fichier `point.txt` les futurs points de consignes.
Ils sont de la forme :

    x y z
    x y z
    ...

### Configuration du port de l’Arduino

Dans un premier temps on regarde le port de l’arduino. Pour cela dans l’application Arduino, on le trouve facilement dans outils/port.
Souvent le port est `ttyACM0`. On retient alors `ACM0`.

PS : Si plusieurs cartes ont été connectées, il est probable que le port soit `ACM1`, etc …

De plus on vérifie le baudrate de la carte.

### Lancement de ROS

Puis on configure le robot, pour cela on modifie dans le fichier `src/navigation_valrob/launch/robot.launch` les paramètres de la carte :

    portCarte : "ACM0"
    bauderate : 115200


Maintenant on lance les nodes ROS :

    roslaunch navigation_valrob robot.launch 

Le robot devrait alors commencer à bouger vers les points souhaités.

``` note:: Lorsque l’on écrit au clavier, il est utile d’utiliser la touche tabulation. Cela permet de compléter automatiquement la commande en cours.
```