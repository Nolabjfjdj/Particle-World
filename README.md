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

Version prototype 0.3.6. Le mode Music Maze convertit les événements MIDI en temps avec une carte de changements de tempo, déplace le rectangle à vitesse constante entre les blocs, avec des distances proportionnelles aux intervalles MIDI, et déclenche chaque note au contact. Le générateur vérifie les segments contre les anciens blocs et impose au rectangle de repartir du bloc touché vers l'extérieur, sans le traverser. Le parcours est réparti dans un grand espace 2D et complété par des blocs décoratifs sans note. Le carré garde une couleur unie qui évolue progressivement dans le spectre arc-en-ciel, avec une teinte de départ aléatoire à chaque réinitialisation. Le Music Maze utilise un fond bleu nuit et un décor de grandes structures compactes en blocs noirs connectés, placées autour et à proximité des blocs de notes, en amas compacts plus proches des blocs de notes, avec des rectangles verticaux allongés de taille uniforme (14 × 42 px), alignés sur une même grille droite, avec des couloirs sinueux beaucoup plus larges et des zones ouvertes. Les blocs de notes sont de minuscules rectangles de 3 × 8 px orientés selon le bord du bloc de décor le plus proche et placés sur son arête. Ils se confondent avec le mur avant le contact. Chaque contact déclenche une petite gerbe de particules colorées qui disparaît en environ trois secondes. Les rectangles se chevauchent légèrement et sont dessinés sans contours internes afin d'éviter les traits et les petits espaces visibles entre les blocs. Les couloirs sont creusés visuellement dans les structures, qui restent décoratives et ne bloquent pas le parcours. Les blocs de notes sont des rectangles verticaux de 7 × 16 px, restent sombres jusqu'au contact, puis gardent leur couleur lumineuse. À chaque contact, le carré produit un impact coloré, grossit brièvement et s'étire perpendiculairement à sa direction d'arrivée avant de reprendre sa forme carrée. La physique des rebonds reste à développer.
