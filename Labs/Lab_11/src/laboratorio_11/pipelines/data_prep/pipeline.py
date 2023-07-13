"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.11
"""
from kedro.pipeline import Pipeline, node

from .nodes import (
    create_model_input_table,
    get_data,
    preprocess_companies,
    preprocess_shuttles,
)


def create_pipeline(**kwargs) -> Pipeline:

    return Pipeline(
        [
            node(get_data, inputs=None, outputs=["companies", "shuttles", "reviews"]),
            node(
                preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
            ),
            node(
                preprocess_shuttles, inputs="shuttles", outputs="preprocessed_shuttles"
            ),
            node(
                create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
            ),
        ]
    )
