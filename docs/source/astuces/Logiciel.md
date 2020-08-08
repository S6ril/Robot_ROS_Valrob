# Logiciel

Pour coder je suis sous Ubuntu.

## VScode

Mon éditeur de code est [visual studio code](https://code.visualstudio.com/Download). J’utilise la version `snap` car elle est automatiquement mise à jour. 

### Addons

J’utilise les extensions suivantes :

- Arduino : pas facile à configurer
- arduino-snippets : permet d’avoir une auto-completion pour arduino
- Atom Keymap : raccourcis Atom
- C/C++ : classique
- Doxygen Documentation : permet d’avoir des commentaires pour une documentation automatique en C/C++ avec doxygen
- GitHub : classique
- Python : classique
- Python Docstring Generator : permet d’avoir des commmentaires python pour la documentation automatique
- ROS
- Visual Studio Intellicode : auto-completion performante de Microsoft

#### Arduino addon

J’ai installé arduino idle avec `snap`. Si une erreur incessante apparait pour l’addon arduino, il faut rajouer dans les configurations :

    "arduino.path": "/snap/arduino/current",

Cela permet d’indiquer où se trouve l’installation d’arduino idle.

## Terminal

J’utilise Terminator comme terminal. Il est plus puissant que celui d’origine, car il a la possibilité de créer plusieurs terminaux dans une fenètre.

    sudo apt install terminator


