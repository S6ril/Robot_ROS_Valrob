# Lancement rapide



Maintenant que le code est prêt, il faut le lancer. Pour cela, j’utilise un [ROSLaunch](https://wiki.ros.org/roslaunch/Commandline%20Tools/) qui me permet de lancer un Roscore et des nodes simultanément.

    cd catkin_ws/
    catkin_make
    source ./devel/setup.bash  

La dernière commande permet « d’apprendre » au terminal toutes les nouvelles commandes contenue dans ce dossier.

## Configuration

### Itinéraire

On configure dans le fichier `point.txt` les futurs points de consignes.
Ils sont de la forme :

    x y z
    x y z
    ...

### Robot

#### Port de l’Arduino

Dans un premier temps on regarde le port de l’arduino. Pour cela dans l’application Arduino, on le trouve facilement dans outils/port.
Souvent le port est `ttyACM0`. On retient alors `ACM0`.

PS : Si plusieurs cartes ont été connectées, il est probable que le port soit `ACM1`, etc …

De plus on vérifie le bauderate de la carte.

#### Lancement de ROS

Puis on configure le robot, pour cela on modifie dans le fichier `src/navigation_valrob/launch/robot.launch` les paramètres de la carte :

    portCarte : "ACM0"
    bauderate : 115200


Maintenant on lance les nodes ROS :

    roslaunch navigation_valrob robot.launch 

Le robot devrait alors commencer à bouger vers les points souhaités.

``` note:: Lorsque l’on écrit au clavier, il est utile d’utiliser la touche tabulation. Cela permet de compléter automatiquement la commande en cours.
```