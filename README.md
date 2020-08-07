
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/S6ril/Robot_ROS_Valrob/blob/master/images/logo_valrob.PNG">
    <img src="images/logo_valrob.png" alt="Logo" width="150" >
  </a>

  <h3 align="center">Robot ROS - Valrobotik - ENSIAME Valenciennes </h3>

  <p align="center">
    Un projet pour rendre le robot modulaire !!
    <br />
    <a href="https://s6ril.github.io/Robot_ROS_Valrob/"><strong>Documentation »</strong></a>
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
# Sommaire

* [Cette branche](#cette-branche)
  * [Construit avec](#construit-avec)
* [Pour commencer](#pour-commencer)
  * [Prerequis](#prerequis)
  * [Installation de ROS sur Ubuntu](#installation-de-ros-sur-ubuntu)
  * [Préparation de l’environnement ROS](#préparation-de-lenvironnement-ros)
  * [Github](#github)
* [Utilisation](#utilisation)
* [Licence](#licence)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)





<!-- ABOUT THE PROJECT -->
# Cette branche

<p align="center">
 <a href="https://github.com/S6ril/Robot_ROS_Valrob/blob/master/images/tortue_exemple.gif">
    <img src="images/tortue_exemple.gif" alt="Gif" >
  </a>
</p>

Ce projet a pour but d’initier l’intégration du langage ROS pour le robot Valrob. Cela s’inscrit dans une démarche de rendre le robot modulaire et d’avoir une base solide pour les autres annnées.

Cette branche est une DEMO. On simule le Robot par le biais d’une Tortue (turtle_sim). En entrant les points dans le fichier `point.txt`. La tortue se déplacera automatiquement vers chacun de ces points.


## Construit avec
Ce robot a été développé avec ROS. On retrouve alors :
* [ROS Noetic](https://www.ros.org/)
* [Python 3](https://www.python.org/)
* Dans mon cas l’OS est [Ubuntu 20 LTS](https://ubuntu.com/download/desktop)



<!-- GETTING STARTED -->
# Pour commencer

## Prerequis

ROS et Python doivent être installés.

Pour l’installation de ROS sur une autre plateforme, il faut suivre ce [tutoriel](http://wiki.ros.org/noetic/Installation).

## Installation de ROS sur Ubuntu

Je me base sur le [tutoriel de ROS](http://wiki.ros.org/noetic/Installation/Ubuntu) pour l’installation sous Ubuntu.

On ajoute le dépot :

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
    sudo apt update

On installe ROS :
    
    sudo apt install ros-noetic-desktop-full


On peut ajouter au terminal l’environnement ROS :
    
    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc


## Préparation de l’environnement ROS

Je me base sur le [tutoriel de ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).

Il faut dans un premier temps sourcer le terminal (si ce n’est pas déjà fait) :
    
    source /opt/ros/noetic/setup.bash


Puis créer le ROS Workspace :

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
  
On impose python 3 pour `catkin_make`. ROS Noetic est le premier ROS à être seulement basé sur Python3. Pour cette version `catkin_make` suffit.

On source à nouveau le workspace (pour prendre en compte les modofications) :

    source devel/setup.bash


On peut alors mettre le code github sur l’ordinateur !

## Github

Pour récupérer les fichiers de Github :

    git clone -b Demo_turtle https://github.com/S6ril/Robot_ROS_Valrob.git

(On clone seulement la branche Demo_turtle qui correspond à la branche de démo avec la tortue.)

Puis on copie le dossier cloné vers `catkin_ws/` :
    
    cd ~
    cp -r Robot_ROS_Valrob/* catkin_ws/


On peut alors effectuer un `catkin_make` :

    cd ~/catkin_ws
    catkin_make

<!-- USAGE EXAMPLES -->
# Utilisation

Avant de lancer le pogramme, on définit les points voulus dans le fichier `point.txt`. Ils sont de la forme :
    
    x y z
    x y z 
    ...

Pour lancer le programme, on execute ROS :
    
    cd ~/catkin_ws 
    roslaunch navigation_valrob turtle.launch


La tortue va alors se diriger vers chacun des points !


<!-- LICENSE -->
# Licence

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
# Contact

S6ril & Starfunx

Valrobotik - ENSIAME Valenciennes

Lien du projet : [https://github.com/S6ril/](https://github.com/S6ril/Robot_ROS_Valrob.git)



<!-- ACKNOWLEDGEMENTS -->
# Acknowledgements
* [Template](https://github.com/othneildrew/Best-README-Template)


