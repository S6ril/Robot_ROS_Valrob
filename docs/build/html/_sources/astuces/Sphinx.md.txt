# Sphinx



## Faire sa documentation avec Sphinx
Toute cette documentation a été faite avec [Sphinx](https://www.sphinx-doc.org/en/master/). 

À première vue c’est assez complexe, mais ce n’est pas irréalisable pour un futur ingénieur INSA HDF !!!

## Installation de Sphinx

Je me base sur ce [site](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/). Il explique plutôt bien la procédure. Comme d’habitude, je suis sous Ubuntu 20 LTS.

Pour cela on utilise pip :

    pip3 install Sphinx

Pour plus tard, on installe aussi une extension pour écrire en Mardown (plus pratique que le `.rst`) :

    pip3 install recommonmark

Il faut aussi installer un thème :

    pip3 install sphinx-rtd-theme


C’est déjà fini !!

## Configuration

C’est la partie la plus délicate. Je me base sur cette documentation. Elle a été faite dans le dossier source `catkin_ws`. On crée alors un nouveau document :

    cd ~/catkin_ws/
    mkdir docs/
    sphinx-quickstart
    
Une liste de question va alors apparaitre (lorsque c’est vide, il faut faire `entrer`, cela laisse la valeur par défaut):
```bash
    > Separate source and build directories (y/n) [n] : y
    > Name prefix for templates and static dir [_] :
    > Project name : À choisir
    > ...
    ...
    > Project language [en : fr
    > Name of your master document (without suffix) [index] :
    > autodoc : automatically insert docstrings from modules (y/n) [n] : y
    > ...
```

Ajouter les extensions que vous voulez !!

Maintenant que cela est fait, on se rend dans le dossier `source` et on va modifier `conf.py`. Cela permettra de mieux configurer Sphinx.

Tout d’abord en haut, on rajoute :

    import os
	import sys
	sys.path.insert(0, os.path.abspath('./../../src/navigation_valrob/script/'))

Cela permet d’ajouter le dossier qui contient les différents scripts Pythons.

En même temps, on ajoute :

    import recommonmark
    from recommonmark.transform import AutoStructify
    from recommonmark.parser import CommonMarkParser

Cela permet d’écrire la documentation en langage markdown.
Pour les extensions, on ajote dans la ligne `recommonmark`.

    extensions = [
    	'sphinx.ext.autodoc',
		...    	
		'recommonmark',
    ]


On modifie la ligne `source_suffix` par :

    source_suffix = {
    	'.rst': 'restructuredtext',
    	'.md': 'markdown',
	}

On ajoute en dessous :

    source_parsers = {
        '.md': CommonMarkParser
    }

et en bas du document :

    github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
    def setup(app):
        app.add_config_value('recommonmark_config', {
                'url_resolver': lambda url : github_doc_root + url,
                'auto_toc_tree_section': 'Contents',
                }, True)
        app.add_transform(AutoStructify)

Ce n’est pas facile, mais le mardown est bien pratique pour écrire la documentation.

Il est aussi conseiller de changer le thème de la page, pour cela j’utilise [sphinx rtd theme](https://github.com/readthedocs/sphinx_rtd_theme). On modifie la ligne.

    html_theme = 'sphinx_rtd_theme'

Il en existe d’autre sur internet.

J’ajoute par la même occasion un logo (ajouter la ligne juste en dessous) :

    html_logo = "./../../images/robot.png"

Et ma page est configurée. Si le doute persiste, mon fichier de configuration se trouve sous Github.


## Lancement du script

Avec cette configuration, on génère la documentation automatiquement. Dans un premier temps, on link les scripts pythons. 

	cd ~/catkin_ws/docs
    sphinx-apidoc -o source/ ~/catkin_ws/src/navigation_valrob/script/


Il faudra avant de lancer la compilation modifier le fichier `index.rst`, et ajouter `modules` :

    .. toctree::
	   :maxdepth : 2
	   :caption : Sommaire :

	   modules


Maintenant on peut compiler :

    make clean html


Le site est maintenant accessible dans le dossier `docs\build\html\index.html`.


## Pour aller plus loin

### Page Github documentation

Github permet de gérer des pages de documentations. Mais avec cette astuce, `index.html` doit se situer dans le dossier `docs`. Pour cela, il suffit de créer une page `index.html` qui redirige vers la page Sphinx de documentation.

    cd ~/catkin_ws/docs
    echo '<meta http-equiv="refresh" content="0; url=./build/html/index.html" />' >> index.html

Maintenant sous Github, il suffit d’aller dans les options du repo, et d’activer `Github Pages` avec le dossier `/docs`.
La redirection est automatique.

### Lisibilité des fichiers sources

Pour plus de lisibilité, j’ai choisi de séparer mes chapitres dans le site dans des sous-dossier. Pour cela, j’ai créé un dossier `script`, j’ai inserer les fichiers `.rst` correspondant dedans. Et dans le fichier `modules.rst`, je modifie le chemin d’accès. Exemple :

    script/Consigne_point

Cela rend mon répertoire plus lisible !!