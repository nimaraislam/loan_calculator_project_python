from typing import Optional
from pydantic import BaseModel, Field
from pydantic.types import constr

LoanDurationType=constr(to_upper=True,pattern='^[YM]$')


class LoanUpdateSchema(BaseModel):
    principal_amount: float = Field(..., gt=0,description="Amount that customer wants to borrow.", json_schema_extra={"example": 1000.00})
    interest_rate: float = Field(..., gt=0,description="Interest rate which customer needs to pay monthly", json_schema_extra={"example": 1.00})
    term: int = Field(..., gt=0,description="The length of time until a loan is due", json_schema_extra={"example": 1})
    month_or_year: LoanDurationType = Field(...,description="Term in year or month", json_schema_extra={"example": "Y"})

class LoanSchema(BaseModel):
    id: int
    principal_amount: float
    interest_rate: float
    term: int
    month_or_year: LoanDurationType
    total_interest: float
    final_amount: float