
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/S6ril/Robot_ROS_Valrob/blob/master/images/logo_valrob.PNG">
    <img src="images/logo_valrob.png" alt="Logo" width="100%" >
  </a>

  <h3 align="center">Robot ROS - Valrobotik - ENSIAME Valenciennes </h3>

  <p align="center">
    Un projet pour rendre le robot modulaire !!
    <br />
    <a href="https://s6ril.github.io/Robot_ROS_Valrob/"><strong>Documentation »</strong></a>
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Cette Branche](#branche)
* [Le Projet](#projet)
  * [Construit avec](#construit)
* [Pour commencer](#commencer)
  * [Prérequis](#prerequis)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)


## Cette Branche

Cette branche est une branche de TEST. Elle permet à partir d'un Joystick, d'une Raspberry et d'une Arduino de controller un robot en passant par des nodes ROS. 


<p align="center">
  <a href="https://github.com/S6ril/Robot_ROS_Valrob/blob/Robot_test/images/Node_Robot_Test.png">
    <img src="images/Node_Robot_Test.png" alt="Logo" width="150" >
  </a>
</p>




## Construit avec
Ce robot à dont été développer avec ROS. On retrouve alors :
* [ROS Noetic](https://www.ros.org/)
* [Python 3](https://www.python.org/)
* [Arduino](https://www.arduino.cc/)
* [Raspberry Pi 3](https://www.raspberrypi.org/) avec [Ubuntu Server](https://ubuntu.com/download/raspberry-pi) comme OS





<!-- GETTING STARTED -->
# Pour commencer

## Préparation de la Raspberry Pi

Cela est un résumé de l'installation décrit par Ubuntu. Voir le [lien](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi) pour plus de détails.

Dans mon cas, j'utilise une Raspberry Pi 3b avec 1Go de RAM. Je prends alors la version 32 bits de l'os. Je prépare la carte SD avec Raspberry Pi Imager.

Après le flash, il faut modifier dans la partition `system-boot` le fichier `network-config` et décommanter (et adapter) les lignes suivantes :

    wifis:
      wlan0:
      dhcp4: true
      optional: true
      access-points:
        "home network":
          password: "123456789"


Maintenant la Raspberry peut être démarrée. L'os est configuré pour activer automatiquement la connection SSH.
L'utilisateur et mot de passe par défaut est `ubuntu`. 

<div class="panel panel-warning">
**Attention**
{: .panel-heading}
<div class="panel-body">

Le clavier est surement en qwerty !!

</div>
</div>


Pour changer le clavier en français, je me base sur ce [site](https://linoxide.com/linux-how-to/configure-keyboard-ubuntu/).

En une ligne la commande est :

    L='fr' && sudo sed -i 's/XKBLAYOUT=\"\w*"/XKBLAYOUT=\"'$L'\"/g' /etc/default/keyboard

Par habitude, on peut aussi verifier les mises à jours :

    sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y


Comme l'installation de ubuntu est minimale, il faut installer le paquet `build-essential`

    sudo apt install build-essential


La Raspberry est enfin prête pour pouvoir installer ROS.

## Installation de ROS

Je me base sur le [tutoriel de ROS](http://wiki.ros.org/noetic/Installation/Ubuntu) pour installation sous Ubuntu.

Sur la Raspberry il n'est pas utile d'installer entièrement ROS, mais seulement les paquets essentiels. 
On ajout le dépot :

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
    sudo apt update

On installe ROS base :
    
    sudo apt install ros-noetic-ros-base

Pour la manette il faut installer le paquet `ros-joystick-drivers` :

    sudo apt install ros-noetic-joystick-drivers

On peut ajouter au terminal l'environnement ROS :
    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc


## Préparation de l'environnement ROS

Je me base sur le [tutoriel de ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).

Il faut dans un premier temps sourcer le terminal (si ce n'est pas déjà fait) :
    
    source /opt/ros/noetic/setup.bash


Puis créer le ROS Workspace :

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
  
On impose python 3 pour `catkin_make`.

On source à nouveau le workspace (pour prendre en compte les modofications) :

    source devel/setup.bash


On peut alors copier le github sur la raspberry :

## Github

Pour récupérer les fichiers de Github :

    git clone -b Robot_test https://github.com/S6ril/Robot_ROS_Valrob.git

(On clone seulement la branche Robot_test qui correspond à la branche de démo avec le joystick.)

# Utilisation

## Prerequis

ROS et Python doivent être installés sur la Raspberry.


<!-- USAGE EXAMPLES -->
## Usage

Pour lancer le programme sur un ordinateur :
```bash
roslaunch navigation_valrob robot.launch 
```

_Pour plus de précision, veuillez vous réferer à la [Documentation](https://s6ril.github.io/Robot_ROS_Valrob/)_




<!-- LICENSE -->
## Licence

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

S6ril & Starfunx

Valrobotik - ENSIAME Valenciennes

Lien du projet : [https://github.com/S6ril/](https://github.com/S6ril/Robot_ROS_Valrob.git)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Template](https://github.com/othneildrew/Best-README-Template)


