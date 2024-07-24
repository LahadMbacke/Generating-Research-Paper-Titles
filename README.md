# Projet de Génération de Titres pour Articles Scientifiques

Ce projet consiste à générer des titres pour des articles scientifiques en utilisant un modèle GPT-2 fine-tuné. Le processus se divise en plusieurs étapes :

1. **Web Scraping des Titres d'Articles**
2. **Nettoyage des Données**
3. **Fine-tuning du Modèle GPT-2**
4. **Génération de Titres**

## Prérequis

- Python 3.x
- Les bibliothèques suivantes :
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `transformers`
  - `torch`
  - `accelerate`

Vous pouvez installer les bibliothèques nécessaires en utilisant pip :

```bash
pip install requests beautifulsoup4 pandas transformers torch accelerate

### Explications :

- **Web Scraping** : Le script `web_scraping.py` extrait des titres d'articles d'ArXiv et nettoie ces titres.
- **Fine-Tuning** : Le script `finetuning.py` entraîne le modèle GPT-2 sur les titres nettoyés.
- **Génération de Titres** : Le script `main.py` utilise le modèle fine-tuné pour générer des titres à partir d'un prompt donné.

Assurez-vous de bien adapter le script `clean_data.py` et d'ajuster les chemins des fichiers en fonction de votre environnement de travail.
