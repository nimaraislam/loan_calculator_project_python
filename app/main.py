from fastapi import FastAPI
from app.routers import loans

app = FastAPI()

app.include_router(loans.router)