Fichiers sources détaillés
==========================

Dans cette section, on retrouve tous les fichiers sources de code. 
La documentation est automatique, et basée sur les commentaires des fichiers sources Python. Ces derniers se trouvent dans `src/navigation_valrob/script/`.

N’hésitez pas à regarder le code source. Un petit lien `source` se trouve après chaques prototypes de fonction.

Cet algorithme se base sur 3 nodes qui communiquent comme le montre le graphe ci-dessous.

.. image:: ./../../images/node_ROS_deplacement.png
    :align: center
    :alt: node ROS

Chaques nodes ROS est composées d'une script :

* node_script
* script

La node permet de gérer les entrées/sorties vers ROS (donc vers les différentes nodes). On retrouve aussi la gestion de la fréquence d'actualisation.

Le script est composé d'une classe, et correspond au code en Python. La classe est codée pour répondre au problème.



.. toctree::
   :maxdepth: 4
   :caption: Sommaire

   script/Consigne_point
   script/Motion_controller
   script/Nav_utiles
   script/driver_baseRoulante
   script/node_consigne_point
   script/node_driver_BaseRoulante
   script/node_motion_controller


Bonne lecture ;)
