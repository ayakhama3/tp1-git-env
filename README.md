# ⚙️ TP1 MLOps – Environnement reproductible et pipeline d'entraînement

Travaux pratiques du module *Déploiement d'applications intelligentes* (EMSI) : mise en place d'un environnement reproductible avec **conda** et d'un premier pipeline d'entraînement versionné avec **Git**.

## 🔑 Contenu
- `environment.yml` : environnement conda `tp1-mlops` (Python 3.10, pandas, scikit-learn, ipykernel, python-dotenv)
- `train.py` : pipeline d'entraînement
  - chargement du jeu **Iris**
  - découpage train / test stratifié (80 / 20, `random_state=42`)
  - entraînement d'un **Random Forest** (100 arbres)
  - sauvegarde du modèle avec **joblib** dans `models/iris_model.pkl`

## 🚀 Utilisation
```bash
conda env create -f environment.yml
conda activate tp1-mlops
python train.py
```

## 🛠️ Stack
Python · scikit-learn · conda · joblib · Git

## 👤 Auteure
Aya Khama · [LinkedIn](https://www.linkedin.com/in/aya-khama-160752387)
