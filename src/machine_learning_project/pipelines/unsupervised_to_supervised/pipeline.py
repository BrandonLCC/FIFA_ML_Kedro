from kedro.pipeline import Pipeline, node, pipeline
from .nodes import create_supervised_datasets

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=create_supervised_datasets,
            inputs=dict(
                clean_dataset="clean_dataset",
                features_regression="params:model_options.features",
                target_regression="params:model_options.target",
                features_classification="params:model_options_classification.features",
                target_classification="params:model_options_classification.target",
                test_size_reg="params:model_options.test_size",
                test_size_class="params:model_options_classification.test_size",
                random_state="params:model_options.random_state",
                stratify_class="params:model_options_classification.stratify"
            ),
            outputs=[
                "X_train_class_unsup", "X_test_class_unsup", 
                "y_train_class_unsup", "y_test_class_unsup",
                "X_train_regression_unsup", "X_test_regression_unsup",
                "y_train_regression_unsup", "y_test_regression_unsup"
                ],
            name="create_supervised_datasets_node"
        )
    ])
