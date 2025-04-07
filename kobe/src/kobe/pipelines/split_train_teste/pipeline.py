"""
This is a boilerplate pipeline 'split_train_teste'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.split_data,
            inputs=dict(
                data="data_filtered",
                target_column="params:target_column"
            ),
            outputs=["train","test"],
            name="split_data_node"
        )
    ])
