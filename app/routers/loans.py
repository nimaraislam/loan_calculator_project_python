from fastapi import APIRouter,HTTPException
from app.schemas.loan_schema import LoanSchema,LoanUpdateSchema
from app.services.loan_service import Loan
from app.services.database import Database
from app.services.file_service import read_db,write_db,DB_PATH
from typing import List

router = APIRouter()
router.database = Database()

@router.post("/loans", response_model=LoanSchema)
def create_loan(loan_data: LoanUpdateSchema):
    loan = Loan( loan_data.principal_amount,
                 loan_data.interest_rate,
                 loan_data.term,
                 loan_data.month_or_year )
    loan.calculate_loan_interest()
    loan.calculate_final_amount()
    router.database.save_loan(loan)
    return LoanSchema(**loan.to_dict())

@router.get("/loans", response_model=List[LoanSchema])
def get_all_list():
    return router.database.get_all_loans()

@router.get("/loans/count", response_model=int)
def get_total_loan_number():
    total_loan= router.database.get_total_loan_number()
    return total_loan

@router.get("/loans/total_principal", response_model=float)
def get_sum_of_principal_amount():
    total= router.database.get_sum_of_principal_amount()
    return total

@router.get("/loans/total_interest", response_model=float)
def get_sum_of_interest_amount():
    total= router.database.get_sum_of_interest_amount()
    return total

@router.get("/loans/total_final_amount", response_model=float)
def get_sum_of_final_amount():
    total= router.database.get_sum_of_final_amount()
    return total

@router.get("/loans/{id}", response_model=LoanSchema)
def get_a_loan_details_by_id(id: int):
    loan = router.database.get_loan_details_by_id(id)
    if not loan:
        raise HTTPException(status_code=404,detail=f"Loan id - {id} is not found")
    return loan

@router.get("/loans/{id}/installment", response_model=float)
def calculate_monthly_installment(id: int):
    total =router.database.calculate_monthly_installment(id)
    if not total:
        raise HTTPException(status_code=404,detail=f"Loan id - {id} is not found")
    return total


@router.put("/loans/{id}", response_model=LoanSchema)
def update_loan(id: int, loan_data: LoanUpdateSchema):
    loans =router.database.get_all_loans()

    for index, loan in enumerate(loans):

        if loan.get("id") == id:
            loan_obj = Loan(
                principal_amount=loan_data.principal_amount,
                interest_rate=loan_data.interest_rate,
                term=loan_data.term,
                month_or_year=loan_data.month_or_year
            )
            loan_obj.calculate_loan_interest()
            loan_obj.calculate_final_amount()
            loan_obj.id = id
            updated_data = loan_obj.to_dict()
            loans[index] = updated_data
            write_db(loans, router.database.db_path)
            return LoanSchema(**updated_data)
    raise HTTPException(
        status_code=404,
        detail=f"Loan with ID {id} not found"
    )


@router.delete("/loans/{id}",response_model=LoanSchema)
def delete_loan(id: int):
    deleted_loan=router.database.delete_loan_by_id(id)
    if deleted_loan is None:
         raise HTTPException(status_code=404, detail=f"Loan with id {id} not found")
    return deleted_loan


    

