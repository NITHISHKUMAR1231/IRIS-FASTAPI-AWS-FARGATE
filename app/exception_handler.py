from fastapi import Request
from fastapi.responses import JSONResponse
from app.custom_exception import PredictionException
from app.logger import logger


async def prediction_exception_handler(
    request: Request,
    exc: PredictionException
):

    logger.error(f"Prediction Error: {exc.message}")

    return JSONResponse(
        status_code=500,
        content={
            "error": exc.message
        }
    )