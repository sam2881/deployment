import pickle
import yaml
from google.cloud import storage

import os

# from final.config.core import config

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/mlops-353417-0d6234ccd6b9.json'
bucket_name = "mlops_artifacts_1"
model_type = "artifacts"
model_filename = "0/7f75e29729e249b088d55bef81550402/artifacts/model/7f75e29729e249b088d55bef81550402.pkl"
mlflow_id = "7f75e29729e249b088d55bef81550402"

name = f"{mlflow_id}.pkl"


def load_model(bucket_name, model_type, model_filename):
    try:
        storage_client = storage.Client()  # if running on GCP
        bucket = storage_client.bucket(bucket_name)
        blob1 = bucket.blob('{}/{}'.format(model_type, model_filename))
        blob1.download_to_filename('model/' + str(name))
        return True, None
    except Exception as e:
        print('Something went wrong when trying to load previous model from GCS bucket. Exception: ' + str(e),
              flush=True)
        return False, e


load_model(bucket_name, model_type, model_filename)
