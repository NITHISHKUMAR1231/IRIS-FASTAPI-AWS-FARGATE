from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.schema import IrisRequest, IrisResponse
from app.predict import predict_flower
from app.custom_exception import PredictionException
from app.exception_handler import prediction_exception_handler
from app.logger import logger


app = FastAPI(
    title="Iris ML API",
    description="Production-ready ML API with logging and exception handling",
    version="1.0"
)


# Register custom exception
app.add_exception_handler(
    PredictionException,
    prediction_exception_handler
)


@app.get("/")
def home():

    logger.info("Home endpoint accessed")

    return {
        "message": "Iris ML API is running"
    }


@app.post("/predict", response_model=IrisResponse)
def predict(data: IrisRequest):

    logger.info("Prediction API called")

    result = predict_flower(data.features)

    return {
        "prediction": result
    }


@app.get("/health")
def health_check():

    logger.info("Health check endpoint called")

    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy"
        }
    )