"""
This is a boilerplate pipeline 'treinamento'
generated using Kedro 0.19.12
"""
import pandas as pd
from pycaret.classification import ClassificationExperiment
from sklearn.metrics import log_loss, f1_score


def best_model_from_comparison(data, session_id):

    exp = ClassificationExperiment()
    exp.setup(data=data, target='shot_made_flag', session_id=session_id)

    best_model = exp.compare_models()

    tuned_model = exp.tune_model(best_model, n_iter=10, optimize='AUC')

    return tuned_model


def logistic_regression_model(data, session_id):

    exp = ClassificationExperiment()
    exp.setup(data=data, target='shot_made_flag', session_id=session_id)

    model = exp.create_model('lr')

    tuned_model = exp.tune_model(model, n_iter=10, optimize='AUC')

    return tuned_model

def train_decision_tree(data, session_id):
    exp = ClassificationExperiment()
    exp.setup(data=data, target='shot_made_flag', session_id=session_id)

    model = exp.create_model('dt')
    tuned_model = exp.tune_model(model, n_iter=10, optimize='AUC')

    return tuned_model



def plot_roc(data, model, session_id, output_filename):

    exp = ClassificationExperiment()
    exp.setup(data=data, target='shot_made_flag', session_id=session_id)

    exp.plot_model(model, plot='auc', save=output_filename)


def get_metrics(data, model, model_type="lr"):
    X = data.drop(columns=['shot_made_flag'])
    y_true = data['shot_made_flag'].values

    # Obtem probabilidade e predições
    y_proba = model.predict_proba(X)[:, 1]
    y_pred = model.predict(X)

    metrics_dict = {
        "log_loss": log_loss(y_true, y_proba)
    }

    if model_type == "dt":
        metrics_dict["f1_score"] = f1_score(y_true, y_pred)

    return {
        key: {'value': val, 'step': 1}
        for key, val in metrics_dict.items()
    }

def evaluate_models(data, lr_model, dt_model):
    lr_metrics = get_metrics(data, lr_model, model_type="lr")
    dt_metrics = get_metrics(data, dt_model, model_type="dt")

    combined_metrics = {}

    # Prefixar os nomes das métricas para evitar conflito
    for key, value in lr_metrics.items():
        combined_metrics[f"lr_{key}"] = value

    for key, value in dt_metrics.items():
        combined_metrics[f"dt_{key}"] = value

    return combined_metrics
