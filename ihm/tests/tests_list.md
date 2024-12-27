# Intitulés de tests pour CreatePatientFolderView

## Tests fonctionnels
- [ ] Vérification de la réponse correcte de tous les composants HMI (champs de saisie, boutons, etc.) dans **CreatePatientFolderView**.
- [ ] Test de la validation des champs requis (nom, prénom, date de naissance, etc.).
- [ ] Test de la navigation fluide entre les étapes de création d’un dossier patient.
- [ ] Vérification des interactions correctes avec les systèmes sous-jacents (sauvegarde des données patient).

## Tests d’utilisabilité
- [ ] Évaluation de l’intuitivité du formulaire de création d’un dossier patient pour les utilisateurs.
- [ ] Identification des éléments susceptibles de causer de la confusion (libellés, navigation, disposition).
- [ ] Validation de l’expérience utilisateur avec un lecteur d’écran (accessibilité).

## Tests de performance
- [ ] Test de la réactivité de l’interface lors de la saisie de données.
- [ ] Mesure du temps de réponse entre l’envoi du formulaire et l’enregistrement des données.

## Tests de sécurité
- [ ] Vérification de l’authentification requise avant l’accès à la vue.
- [ ] Test du chiffrement des données sensibles (numéro de sécurité sociale, par exemple).
- [ ] Simulation d’attaques (injection SQL, cross-site scripting) pour garantir la sécurité.

## Tests d’intégration
- [ ] Vérification de l’enregistrement correct des données via l’API backend.
- [ ] Test des notifications ou confirmations après création d’un dossier (par e-mail ou affichage dans l’interface).
- [ ] Simulation d’erreurs pour vérifier la gestion des échecs de communication.

## Documentation et formation
- [ ] Vérification de la présence d’une documentation claire pour les utilisateurs finaux.
- [ ] Évaluation de la facilité de formation des nouveaux utilisateurs pour cette vue.
