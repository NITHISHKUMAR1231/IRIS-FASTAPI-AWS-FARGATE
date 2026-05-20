from pydantic import BaseModel
from typing import List

class IrisRequest(BaseModel):
    features: List[float]   # [sepal_length, sepal_width, petal_length, petal_width]

class IrisResponse(BaseModel):
    prediction: str