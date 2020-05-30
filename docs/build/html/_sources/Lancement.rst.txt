****************
Lancement rapide
****************


Maintenant que le code est prêt, il faut le lancer. Pour cela, j'utilise un `ROSLaunch <https://wiki.ros.org/roslaunch/Commandline%20Tools/>`_ qui me permet de lancer un Roscore et des nodes simultanément.

::

    cd catkin_ws/
    catkin_make
    . devel/setup.bash  #il faut bien noter le "."


La dernière commande permet "d'apprendre" au terminal toutes les nouvelles commandes contenue dans ce dossier.

Maintenant on lance les nodes ROS :

::
    roslaunch navigation_valrob turtle.launch 


.. note::
    Lorsque l'on écrit au clavier, il est utile d'utiliser la touche `tab`. Cela permet de compléter automatiquement la commande en cours.
