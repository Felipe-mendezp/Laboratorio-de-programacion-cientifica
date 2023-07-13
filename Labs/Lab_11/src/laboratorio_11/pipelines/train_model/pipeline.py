"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node

from .nodes import evaluate_model, split_data, train_model

# config_loader = ConfigLoader("conf")
# parameters = config_loader.get("parameters/train_model.yml")


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                split_data,
                inputs=["model_input_table", "params:split_params"],
                outputs=[
                    "X_train",
                    "X_valid",
                    "X_test",
                    "y_train",
                    "y_valid",
                    "y_test",
                ],
                name="split_data_node",
                tags=["training"],
            ),
            node(
                train_model,
                inputs=[
                    "X_train",
                    "X_valid",
                    "y_train",
                    "y_valid",
                    "params:train_params",
                ],
                outputs="trained_model",
                name="train_model_node",
                tags=["training"],
            ),
            node(
                evaluate_model,
                inputs=["trained_model", "X_test", "y_test"],
                tags=["evaluation"],
                outputs=None,
            ),
        ]
    )
