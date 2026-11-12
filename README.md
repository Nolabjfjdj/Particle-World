# Particle World

Particle World est un terrain de jeu de simulations physiques accessible dans un navigateur.

## Lancer le projet

Python 3 est nécessaire. Depuis le dossier du projet :

```bash
python server.py
```

Ouvrir ensuite http://localhost:8000.

Aucune dépendance Python externe n'est nécessaire.

## Modes disponibles

- **Music Maze** : particules dans un labyrinthe, avec une note synthétique à chaque collision.
- **Orbit Arena** : particules dans une arène circulaire avec des obstacles rotatifs.
- **Particle Flood** : simulation d'un groupe de particules avec collisions.
- **Escape** : arène circulaire avec un compte à rebours.

## Commandes

- Choisir un mode dans le panneau de gauche.
- Modifier la vitesse, le nombre de boules et le volume.
- Utiliser Pause ou Réinitialiser.

## Architecture

- `server.py` : serveur HTTP Python sans dépendance.
- `index.html` : interface.
- `style.css` : présentation responsive.
- `app.js` : moteur de simulation et audio Web Audio.

Le rendu et les animations sont exécutés dans le navigateur afin de rester fluides sur ordinateur et mobile. Python sert au lancement local et pourra accueillir plus tard des outils de génération de niveaux ou de gestion de contenu.

## État

Version prototype 0.1.1. Les modes sont des premières implémentations jouables, à affiner à partir des vidéos de référence.