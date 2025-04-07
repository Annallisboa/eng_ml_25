"""
This is a boilerplate pipeline 'treinamento'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.logistic_regression_model,
            inputs=[
                'train',
                'params:session_id',
            ],
            outputs='lr_model',
            tags=['treinamento']
        ),
        node(
            nodes.train_decision_tree,
            inputs=[
                'train',
                'params:session_id',
            ],
            outputs='dt_model',
            tags=['treinamento']
        ),
        # node(
        #     nodes.plot_roc,
        #     inputs=[
        #         'train',
        #         'lr_model',
        #         'params:session_id',
        #         'params:lr_model_roc_filename',
        #     ],
        #     outputs=None,
        #     tags=['report']
        # ),
        node(
            nodes.get_metrics,
            inputs=[
                'train',
                'lr_model',
            ],
            outputs='lr_metrics',
            tags=['report']
        ),
        node(
            nodes.evaluate_models,
            inputs=["train", "lr_model", "dt_model"],
            outputs="model_metrics",
            name="evaluate_models_node"
        )

    ])
