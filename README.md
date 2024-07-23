# Generating-Research-Paper-Titles

Ce projet innovant vise à produire des titres pour des articles scientifiques en utilisant un modèle GPT-2 entraîné sur plus de 2 000 titres d'articles extraits d'arXiv. Ce projet offre également une opportunité d'apprendre le web scraping, car il est nécessaire d'extraire le texte des articles de recherche pour alimenter le modèle en données d'entraînement.

## Aperçu du projet

L'essence de ce projet réside dans sa capacité à générer des titres convaincants et pertinents pour des articles scientifiques, en exploitant la puissance de GPT-2, un modèle de langage de pointe. En entraînant le modèle sur un ensemble de données de titres d'articles de la base de données arXiv, nous assurons que les titres générés sont non seulement uniques, mais aussi qu'ils maintiennent l'intégrité scientifique et la pertinence attendues dans les cercles académiques.

## Objectifs d'apprentissage

- **Web Scraping** : Apprenez à extraire des titres d'articles à partir de papiers de recherche sur arXiv, une compétence cruciale pour la collecte de données d'entraînement.
- **Traitement du Langage Naturel (TAL)** : Plongez dans le TAL en faisant un fine-tuning du modèle GPT-2 pour comprendre et générer un texte semblable à celui de l'homme.
- **Entraînement de modèle** : Acquérez une expérience pratique dans l'entraînement d'un modèle de langage sur un ensemble de données spécialisé pour atteindre des résultats spécifiques.

## Installation

Avant de pouvoir exécuter le projet, vous devez installer les bibliothèques nécessaires. Cela peut être fait en exécutant la commande suivante :

```bash
pip requests beautifulsoup4 lxml transformers datasets torch accelerate
