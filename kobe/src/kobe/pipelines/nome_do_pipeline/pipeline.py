"""
This is a boilerplate pipeline 'nome_do_pipeline'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.prepare_data,
            inputs=['kobe_dev'],
            outputs='data_filtered',
        ),
    ])
