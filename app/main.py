from fastapi import FastAPI
from app.routers import loans

app = FastAPI(title="Welcome to loan calculation calculator!")

app.include_router(loans.router)