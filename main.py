from fastapi import FastAPI
from app.api.v1.endpoints import predict

app = FastAPI()

app.include_router(predict.router, prefix="/v1", tags=["predict"])
