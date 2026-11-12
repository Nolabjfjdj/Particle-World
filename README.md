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

- **Music Maze** : importe un fichier MIDI, analyse ses notes et génère un parcours visuel synchronisé à la musique. Cette première étape pose les bases du générateur de niveau.
- **Orbit Arena** : particules dans une arène circulaire avec des obstacles rotatifs.
- **Particle Flood** : simulation d'un groupe de particules avec collisions.
- **Escape** : arène circulaire avec un compte à rebours.

## Commandes

- Choisir un mode dans le panneau de gauche.
- Dans Music Maze, importer un fichier .mid ou .midi puis lancer le parcours.
- Modifier la vitesse, le nombre de boules et le volume.
- Utiliser Pause ou Réinitialiser.

## Architecture

- `server.py` : serveur HTTP Python sans dépendance.
- `index.html` : interface.
- `style.css` : présentation responsive.
- `app.js` : moteur de simulation, lecture MIDI et audio Web Audio.

Le MIDI est lu directement dans le navigateur. Aucune dépendance externe ni envoi du fichier vers un serveur n'est nécessaire.

## État

Version prototype 0.2.0. Le mode Music Maze convertit les événements MIDI en temps avec une carte de changements de tempo, déplace le rectangle à vitesse constante entre les blocs, avec des distances proportionnelles aux intervalles MIDI, et déclenche chaque note au contact. Le générateur tente aussi d'éviter que les segments traversent les anciens blocs. Le parcours est réparti dans un grand espace 2D et complété par des blocs décoratifs sans note. La physique des rebonds reste à développer.
