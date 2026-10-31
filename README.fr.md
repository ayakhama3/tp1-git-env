# 🧪 TP1 — MLOps : environnement reproductible & pipeline d'entraînement

[🇬🇧 English](README.md) | 🇫🇷 Français

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?logo=scikit-learn&logoColor=white)
![Conda](https://img.shields.io/badge/Conda-environnement-44A833?logo=anaconda&logoColor=white)

Premier TP sur les fondamentaux du MLOps : mettre en place un **environnement Python reproductible** et exécuter un **pipeline d'entraînement** minimal qui produit un artefact de modèle prêt à être versionné.

## 📌 Ce que fait le projet

`train.py` exécute un petit pipeline de bout en bout :

1. Charge le jeu de données **Iris** (scikit-learn).
2. Le découpe en 80 % / 20 % (stratifié, `random_state=42`).
3. Entraîne un classifieur **Random Forest** (100 arbres).
4. Sauvegarde le modèle dans `models/iris_model.pkl` avec `joblib`.
5. Affiche la précision (accuracy) mesurée sur le jeu de test.

Les graines fixées rendent l'exécution reproductible.

## 📁 Structure

```
tp1-git-env/
├── environment.yml   # Environnement Conda (Python 3.10, pandas, scikit-learn, ...)
├── train.py          # Pipeline d'entraînement
└── models/           # Généré à l'exécution (ignoré par Git)
```

## 🚀 Démarrage

```bash
git clone https://github.com/ayakhama3/tp1-git-env.git
cd tp1-git-env

conda env create -f environment.yml
conda activate tp1-mlops

python train.py
```

Résultat attendu : une ligne confirmant la sauvegarde du modèle dans `models/iris_model.pkl`, suivie de la précision sur le jeu de test.

## 🧰 Stack technique

Python 3.10 · scikit-learn · pandas · joblib · python-dotenv · Conda

## 👩‍💻 Auteure

**Aya Khama** — Étudiante ingénieure Data Science & IA (EMSI)
[LinkedIn](https://www.linkedin.com/in/aya-khama-160752387/) · [GitHub](https://github.com/ayakhama3)
