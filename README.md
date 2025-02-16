# Calculatrice en Microservices

Ce projet est une calculatrice simple divisée en 4 microservices indépendants :
- **Addition** : Effectue l'opération d'addition.
- **Soustraction** : Effectue l'opération de soustraction.
- **Multiplication** : Effectue l'opération de multiplication.
- **Division** : Effectue l'opération de division.

Chaque microservice est conteneurisé avec Docker et peut être déployé localement ou sur le cloud (Azure, AWS, etc.).

---

## Technologies utilisées
- **Langage** : Python
- **Framework** : Flask (pour les API REST)
- **Conteneurisation** : Docker
- **Orchestration** : Docker Compose
- **Cloud** : Azure ou AWS (optionnel)
- **CI/CD** : GitHub Actions ou GitLab CI/CD (optionnel)

---

## Structure du projet

```
calculator/
│
├── addition/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── subtraction/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── multiplication/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── division/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## Comment exécuter le projet

### Prérequis
- Docker installé sur votre machine.
- Docker Compose installé.

### Etapes pour exécuter le projet

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-utilisateur/calculator-microservices.git
   cd calculator-microservices
   ```

2. **Construire et démarrer les conteneurs**
   ```bash
   docker-compose up --build
   ```

3. **Accéder aux microservices**
   - **Addition** : `http://localhost:5001/add?a=10&b=5`
   - **Soustraction** : `http://localhost:5002/subtract?a=10&b=5`
   - **Multiplication** : `http://localhost:5003/multiply?a=10&b=5`
   - **Division** : `http://localhost:5004/divide?a=10&b=5`

4. **Arrêter les conteneurs**
   ```bash
   docker-compose down
   ```

---

## API Documentation

### Addition
- **Endpoint** : `/add`
- **Méthode** : `GET`
- **Paramètres** :
  - `a` : Premier nombre (float).
  - `b` : Deuxième nombre (float).
- **Exemple** :
  ```bash
  curl "http://localhost:5001/add?a=10&b=5"
  ```
  **Réponse** :
  ```json
  {
    "result": 15
  }
  ```

### Soustraction
- **Endpoint** : `/subtract`
- **Méthode** : `GET`
- **Paramètres** :
  - `a` : Premier nombre (float).
  - `b` : Deuxième nombre (float).
- **Exemple** :
  ```bash
  curl "http://localhost:5002/subtract?a=10&b=5"
  ```
  **Réponse** :
  ```json
  {
    "result": 5
  }
  ```

### Multiplication
- **Endpoint** : `/multiply`
- **Méthode** : `GET`
- **Paramètres** :
  - `a` : Premier nombre (float).
  - `b` : Deuxième nombre (float).
- **Exemple** :
  ```bash
  curl "http://localhost:5003/multiply?a=10&b=5"
  ```
  **Réponse** :
  ```json
  {
    "result": 50
  }
  ```

### Division
- **Endpoint** : `/divide`
- **Méthode** : `GET`
- **Paramètres** :
  - `a` : Premier nombre (float).
  - `b` : Deuxième nombre (float).
- **Exemple** :
  ```bash
  curl "http://localhost:5004/divide?a=10&b=5"
  ```
  **Réponse** :
  ```json
  {
    "result": 2
  }
  ```
- **Erreur** : Si `b = 0`, la réponse sera :
  ```json
  {
    "error": "Division by zero"
  }
  ```

---

## Déploiement sur le cloud

### Azure
1. Poussez les images Docker vers Azure Container Registry (ACR).
2. Déployez les conteneurs avec Azure Kubernetes Service (AKS) ou Azure Container Instances (ACI).

### AWS
1. Poussez les images Docker vers Amazon Elastic Container Registry (ECR).
2. Déployez les conteneurs avec Amazon ECS ou EKS.

---

## Pipeline CI/CD

Un pipeline CI/CD peut être configuré avec GitHub Actions ou GitLab CI/CD pour automatiser la construction, les tests et le déploiement des microservices.

Exemple de fichier `.github/workflows/ci-cd.yml` pour GitHub Actions :
```yaml
name: CI/CD Pipeline
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Build Docker images
        run: docker-compose build
      - name: Push to Azure/AWS
        run: |
          echo "Push images to cloud registry"
```

---

## Auteurs
- Maha LAHSSINI
- Nisrine EL MORABITI

---
