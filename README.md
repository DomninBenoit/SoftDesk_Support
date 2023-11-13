# SoftDesk Support

<p align="center">
<img src="./SoftDesk/assets/logo.png" width="100%">
</p>

## Projet

Création d'une API RESTful pour une application permettant de remonter et de suivre des problèmes technique.

## Fonctionnalités

Un visiteur non connecté doit pouvoir :
- s’inscrire ;  
- s'authentifier avec un JSON Web Token. 

Un utilisateur connecté doit pouvoir : 
- Créé un nouveau projet
- Modifier et supprimer un projet dont il est l'auteur
- Ajouter ou supprimer un contributeur d'un projet dont il est l'auteur
- Ajouter une issue ou un commentaires sur un projet dont il est l'auteur ou un contributeur
- Modifier ou supprimer une issue ou un commentaire dont il est l'auteur
- Visualiser les projets dont il est l'auteur ou un contributeur

## Installation

- Python 3.10
- pip 22.3.1

**Cloner le répository suivant**
> https://github.com/DomninBenoit/SoftDesk_Support.git

Installation de l'environnement virtuel 
> python -m venv ENV   

Activation de l'environnement virtuel :
> .\ENV\Scripts\activate

Installation des dépendances:
> pip install -r requirements.txt

Génération de la 'SECRET_KEY' :
- Dans le répertoire contenant 'settings.py', créez un fichier 'settings_secret.py'.
- Utilisez la commande suivante:
> python .\SoftDesk\generate_secret_key.py
- Ecrivez dans le fichier 'settings_secret.py':
> SECRET_KEY = "resultat de la commande python .\SoftDesk\generate_secret_key.py"

## BDD

- création de la BDD
> python manage.py migrate


## Utilisation

- Assurez-vous que l'environnement virtuel est activé, puis lancez le serveur :

> python .\manage.py runserver 

- Depuis votre navigateur, accédez à l'adresse suivante :  
> http://127.0.0.1:8000/



