from fastapi import APIRouter,HTTPException
from app.schemas.loan_schema import LoanSchema
from app.services.loan_service import Loan
from app.services.database import Database
from app.services.file_service import read_db,write_db,DB_PATH
from typing import List

router = APIRouter()
database = Database()

@router.get("/loans", response_model=List[LoanSchema])
def get_all_list():
    return database.get_all_loans()