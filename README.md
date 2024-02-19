# Classic Plus

**World of Warcraft Classic** and **Plus**

# Installation

1. [Python](https://www.python.org/downloads/)
2. Pillow : `pip install Pillow`
3. Customtkinter : `pip install customtkinter` | `pip install customtkinter --upgrade`

# Chat prompt

Création d'un bot pour interagir avec un jeu vidéo comme World of Warcraft en lisant ce qui se passe à l'écran du joueur. Implique généralement des techniques de capture d'écran, de traitement d'image, et de simulation d'entrées utilisateur. Approche utilisant Python comme langage de programmation :

1. **Capture d'écran** : Vous devez d'abord capturer périodiquement l'écran du joueur pour obtenir des informations sur ce qui se passe dans le jeu. Vous pouvez utiliser des bibliothèques Python comme Pillow (PIL) pour la capture d'écran.

2. **Traitement d'image** : Une fois que vous avez une capture d'écran, vous devrez extraire les informations pertinentes en utilisant le traitement d'image. Cela peut inclure la détection d'objets, de textes ou d'éléments spécifiques à l'écran du jeu. Les bibliothèques telles que OpenCV peuvent être utiles pour cette tâche.

3. **Prise de décision** : Après avoir extrait des informations de l'écran, votre bot doit prendre des décisions sur les actions à entreprendre dans le jeu. Cela peut inclure des décisions tactiques ou stratégiques.

4. **Simulation d'entrées** : Une fois que votre bot a pris une décision, il doit simuler des entrées utilisateur pour exécuter ces actions dans le jeu. Cela peut inclure la simulation de mouvements du personnage, de clics de souris, de frappes de clavier, etc.

5. **Boucle de jeu** : Votre bot devra fonctionner en boucle, capturant régulièrement l'écran, prenant des décisions et simulant des entrées pour jouer de manière autonome.

6. **Gestion des données** : Vous devrez également gérer les données collectées par votre bot, surveiller l'état du jeu, gérer les erreurs et les exceptions, etc.

7. **Détection de triche** : Assurez-vous de respecter les conditions d'utilisation du jeu, car l'utilisation de bots ou de scripts automatisés peut être contraire aux règles et entraîner des sanctions.

# Roadmap

Durée estimée: **95 heures** | Temps passé: **4 heures**

**1. Choix des bibliothèques** (4 heures)

- Sélectionnez Pillow (PIL) pour la capture d'écran. (1 heure)
- Envisagez OpenCV pour des fonctionnalités avancées. (2 heures)
- Incluez éventuellement PyAutoGUI pour la simulation d'entrées utilisateur. (1 heure)

**2. Traitement d'image** (20 heures)

- Convertissez les captures d'écran en images numériques. (3 heures)
- Implémentez la détection de contours. (4 heures)
- Appliquez la segmentation. (4 heures)
- Utilisez la reconnaissance de texte avec Tesseract OCR. (5 heures)
- Mettez en place la détection d'objets avec des algorithmes de vision par ordinateur avancés. (4 heures)

**3. Prise de décision** (15 heures)

Analysez la santé du personnage. (2 heures)
Évaluez la position des ennemis. (3 heures)
Examinez les quêtes en cours. (2 heures)
Utilisez des algorithmes d'intelligence artificielle pour des décisions tactiques. (8 heures)

**4. Simulation d'entrées** (20 heures)

Générez des mouvements du personnage. (4 heures)
Interagissez avec l'interface utilisateur du jeu. (4 heures)
Simulez des clics de souris. (4 heures)
Enregistrez des frappes de clavier. (4 heures)
Planifiez des actions complexes pour la stratégie. (4 heures)

**5. Boucle de jeu** (10 heures)

Créez la structure principale pour capturer régulièrement l'écran. (2 heures)
Prenez des décisions en fonction des informations extraites. (2 heures)
Simulez des entrées pour jouer de manière autonome. (6 heures)

**6. Gestion des données** (10 heures)

Sauvegardez les informations collectées par le bot. (2 heures)
Surveillez l'état du jeu. (2 heures)
Gérez les erreurs et les exceptions. (2 heures)
Organisez les fichiers, les logs et les données temporaires. (4 heures)

**7. Éthique et respect des règles du jeu** (5 heures)

Comprenez les conditions d'utilisation du jeu. (1 heure)
Concevez le bot pour respecter ces règles. (2 heures)
Intégrez des mécanismes de sécurité pour éviter la détection. (2 heures)

**8. Tests et débogage** (11 heures)

Gérez correctement les identifiants. (2 heures)
Mettez en place un mécanisme de débogage et de log. (4 heures)
Effectuez des tests de performance. (4 heures)
Utiliser un VPN pour cacher son ip ou autre (1 heure)
