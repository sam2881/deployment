import typing as t

import numpy as np
import pandas as pd

# from regression_model import __version__ as _version
from config.core import config
from processing.data_manager import load_pipeline
from processing.validation import validate_inputs


pipeline_file_name = f"{config.app_config.pipeline_save_file}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None,  "errors": errors}

    if not errors:
        predictions = _price_pipe.predict(
            X=validated_data[config.model_config.features]
        )
        results = {
            "predictions": [np.exp(pred) for pred in predictions],  # type: ignore

            "errors": errors,
        }

    return results
