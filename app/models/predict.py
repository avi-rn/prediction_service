from pydantic import BaseModel

class IrisPredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisPredictionResponse(BaseModel):
    class_name: str
