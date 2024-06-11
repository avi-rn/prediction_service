from fastapi import APIRouter
from app.models.predict import IrisPredictionRequest, IrisPredictionResponse
from app.core.config import load_model
import xarray as xr

router = APIRouter()

model = load_model()
class_names = ["setosa", "versicolor", "virginica"]

@router.post("/predict", response_model=IrisPredictionResponse)
def predict(request: IrisPredictionRequest):
    data = xr.DataArray(
        [[request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]],
        dims=["samples", "features"],
        coords={"samples": [0], "features": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]}
    )
    prediction = model.predict(data.values)
    class_name = class_names[prediction[0]]
    return IrisPredictionResponse(class_name=class_name)
