"""
This is a boilerplate pipeline 'aplicacao'
generated using Kedro 0.19.12
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_prod_data, load_model_from_mlflow, predict_and_evaluate

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_prod_data,
            inputs="kobe_prod",
            outputs="prod_df",
            name="load_prod_data_node"
        ),
        node(
            func=load_model_from_mlflow,
            inputs="params:model_uri",
            outputs="dt_model_loaded",
            name="load_model_node"
        ),
        node(
            func=predict_and_evaluate,
            inputs=["prod_df", "dt_model"],
            outputs="avaliacao_prod",
            name="predict_and_evaluate_node"
        )
    ])

