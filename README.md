# 🧪 TP1 — MLOps: Reproducible Environment & Training Pipeline

🇬🇧 English | [🇫🇷 Français](README.fr.md)

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?logo=scikit-learn&logoColor=white)
![Conda](https://img.shields.io/badge/Conda-environment-44A833?logo=anaconda&logoColor=white)

First practical lab (TP 1) on MLOps fundamentals: set up a **reproducible Python environment** and run a minimal **training pipeline** that produces a versioned-ready model artifact.

## 📌 What it does

`train.py` runs a small end-to-end pipeline:

1. Loads the **Iris** dataset (scikit-learn).
2. Splits it 80 % / 20 % (stratified, `random_state=42`).
3. Trains a **Random Forest** classifier (100 trees).
4. Saves the model to `models/iris_model.pkl` with `joblib`.
5. Prints the accuracy measured on the test set.

Fixed seeds make the run reproducible.

## 📁 Structure

```
tp1-git-env/
├── environment.yml   # Conda environment (Python 3.10, pandas, scikit-learn, ...)
├── train.py          # Training pipeline
└── models/           # Generated at runtime (git-ignored)
```

## 🚀 Getting started

```bash
git clone https://github.com/ayakhama3/tp1-git-env.git
cd tp1-git-env

conda env create -f environment.yml
conda activate tp1-mlops

python train.py
```

Expected output: a line confirming the model was saved to `models/iris_model.pkl`, followed by the test accuracy.

## 🧰 Tech stack

Python 3.10 · scikit-learn · pandas · joblib · python-dotenv · Conda

## 👩‍💻 Author

**Aya Khama** — Data Science & AI engineering student (EMSI)
[LinkedIn](https://www.linkedin.com/in/aya-khama-160752387/) · [GitHub](https://github.com/ayakhama3)
