[![Run Tests](https://github.com/rachidje/medisecure/actions/workflows/run-tests.yaml/badge.svg)](https://github.com/rachidje/medisecure/actions/workflows/run-tests.yaml)
![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)
![TDD](https://img.shields.io/badge/TDD-Test%20Driven%20Development-brightgreen?logo=testcafe)
![Tests Unitaire](https://img.shields.io/badge/tests-unit-green?style=flat-square)
![E2E Tests](https://img.shields.io/badge/tests-e2e-yellow?style=flat-square)
[![codecov](https://codecov.io/gh/rachidje/medisecure/graph/badge.svg?token=ZT5V9MA8C0)](https://codecov.io/gh/rachidje/medisecure)
![Docker](https://img.shields.io/badge/docker-available-blue?logo=docker)
![Stars](https://img.shields.io/github/stars/rachidje/medisecure?style=social)


## MediSecure

MediSecure est un projet de refonte du système d'information d'un établissement de santé privé, visant à moderniser la gestion des dossiers médicaux, améliorer les performances et garantir la conformité réglementaire.

- 🧪 **Approche TDD** (Test Driven Development) 
- 🔍 **Tests unitaires** et **tests E2E** 
- 🐍 **Python 3.12** 
- 📦 **Conteneur Docker** 
- 🔥 **CI/CD GitHub Actions**

## Objectifs

- Centraliser les dossiers médicaux des patients.
- Gérer les rendez-vous et les plannings médicaux.
- Faciliter le suivi des prescriptions et des traitements.
- Offrir une communication sécurisée entre les professionnels de santé.
- Intégrer les laboratoires d'analyses et l'imagerie médicale.
- Optimiser la facturation et la gestion administrative.

## Architecture
MediSecure repose sur une architecture hexagonale, couplée à des microservices et une approche TDD (Test Driven Development). Les choix technologiques et architecturaux incluent :

- Domain-Driven Design (DDD) pour structurer le domaine métier.
- Patterns avancés tels que CQRS, Event Sourcing, et Saga Pattern.
- Accessibilité WCAG 2.1 niveau AA pour garantir l'inclusivité.

## Technologies et outils utilisés
- Langage : Python 3.12
- Frameworks : FastAPI, PYQT6, SQLAlchemy, MySQL
- CI/CD : GitHub Actions
- Conteneurisation : Docker
- Gestion de la sécurité : SAST, DAST, scans de dépendances, tests de pénétration
- Tests : Unités, E2E via Testcontainers


## **Fonctionnalités**

- [x] **Création d'un dossier patient** : Permet de créer et d'enregistrer les informations d'un nouveau patient dans le système.
- [ ] **Gestion des rendez-vous** : Planification des rendez-vous médicaux avec prise en compte des disponibilités.
- [ ] **Suivi des prescriptions et traitements** : Historique et suivi des prescriptions médicales et traitements en cours.
- [ ] **Communication sécurisée entre professionnels de santé** : Messagerie intégrée avec chiffrement des données.
- [ ] **Intégration avec les laboratoires et imagerie médicale** : Connexion directe pour récupérer les résultats d'analyses.
- [ ] **Facturation et gestion administrative** : Génération de factures et gestion des paiements.
- [ ] **Mode hors-ligne** : Fonctionnalités accessibles sans connexion internet.
- [ ] **Support multi-langues** : Interface disponible en plusieurs langues.
- [ ] **Accessibilité** : Compatibilité avec les technologies d’assistance, conforme à la norme WCAG 2.1 niveau AA.


## **Installation**

```bash
git clone https://github.com/rachidje/medisecure.git
cd medisecure
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat  # Windows
pip install -r requirements.txt
```