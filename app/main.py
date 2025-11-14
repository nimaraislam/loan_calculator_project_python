from fastapi import FastAPI
from app.routers import loans

app = FastAPI(title="Welcome to the loan calculation calculator!")

@app.get("/")
def read_root():
    return {"Welcome to loan the calculation calculator!"}


app.include_router(loans.router)
