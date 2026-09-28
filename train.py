from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

MODEL_PATH = Path(__file__).parent / "models" / "iris_model.pkl"


def execute_pipeline():
    print("[MLOps Pipeline] Starting pipeline execution...")

    # Chargement des données
    df = load_iris(as_frame=True).frame
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Entraînement
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)

    # Sauvegarde du modèle
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(classifier, MODEL_PATH)

    accuracy = classifier.score(X_test, y_test)
    print(f"[MLOps Pipeline] Model saved to {MODEL_PATH} | Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    execute_pipeline()