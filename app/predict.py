import pickle
import numpy as np

from app.logger import logger
from app.custom_exception import PredictionException


try:
    model = pickle.load(open("app/model.pkl", "rb"))
    logger.info("Model loaded successfully")

except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise PredictionException("Model loading failed")


labels = ["setosa", "versicolor", "virginica"]


def predict_flower(features: list):

    try:

        logger.info(f"Received input: {features}")

        # Convert input
        input_data = np.array(features).reshape(1, -1)

        # Prediction
        prediction = model.predict(input_data)[0]

        result = labels[prediction]

        logger.info(f"Prediction result: {result}")

        return result

    except Exception as e:

        logger.error(f"Prediction failed: {str(e)}")

        raise PredictionException("Prediction failed")