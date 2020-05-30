*********
Prérequis
*********

.. warning::
    Ce Robot a été développé sous Linux (Ubuntu 20.04 lts) et `ROS Noetic <https://wiki.ros.org/noetic/>`_. Les commandes dans ce tutoriel seront donné pour cet OS. 
    Cependant ROS est un langage disponible sur toutes les plateformes. **Les commandes données pour ROS peuvent varier d'une version à l'autre.**



.. image:: ./../../images/noetic.png
    :width: 200px
    :align: center
    :alt: alternate text
    

Installation
############

ROS
*********************

| Pour installer ROS, il faut suivre le wiki ROS associée à la version utilisée.
| Pour mon cas ce ce sera `ROS Noetic <https://wiki.ros.org/noetic/>`_.

Python
*******************
Voici la page de téléchargement de `Python <https://www.python.org/downloads/>`_.


Téléchargement des codes
########################

Une fois les langages installés, il faut récupérer le code de Github.
On ouvre un terminal, et on crée un nouveau dossier : 
::

    mkdir catkin_ws
    cd catkin_ws

Puis on télécharge le code :

::

    git clone https://github.com/S6ril/Robot_ROS_Valrob.git

C'est bon !! Il reste plus qu'à le lancer.