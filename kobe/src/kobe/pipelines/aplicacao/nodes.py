"""
This is a boilerplate pipeline 'aplicacao'
generated using Kedro 0.19.12
"""
import mlflow.pyfunc
import pandas as pd
from sklearn.metrics import log_loss, f1_score

def load_prod_data(data: pd.DataFrame) -> pd.DataFrame:
    # Apenas retorna o DataFrame que o Kedro vai carregar via catalog
    return data


def load_model_from_mlflow(model_uri: str):
    return mlflow.pyfunc.load_model(model_uri)


def predict_and_evaluate(data: pd.DataFrame, model) -> pd.DataFrame:
    y_true = data["shot_made_flag"]
    X = data.drop(columns=["shot_made_flag"])

    y_proba = model.predict_proba(X)[:, 1]
    y_pred = model.predict(X)

    metrics = {
        "log_loss": log_loss(y_true, y_proba),
        "f1_score": f1_score(y_true, y_pred)
    }

    return pd.DataFrame([metrics])
