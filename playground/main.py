from fastapi import FastAPI
from app.decorators.decorators import router
from app import routes

app = FastAPI()

app.include_router(router)
