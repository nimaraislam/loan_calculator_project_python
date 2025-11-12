from typing import Optional
from pydantic import BaseModel, Field
from pydantic.types import constr

LoanDurationType=constr(to_upper=True,pattern='^[YM]$')
class LoanSchema(BaseModel):
    id:Optional[int] = Field(None,description= "Id of a customer.")
    principal_amount:float = Field(...,gt=0,description="Amount that customer wants to borrow.")
    interest_rate:float=Field(...,gt=0,description="Interest rate which customer needs to pay monthly")
    term:int=Field(...,gt=0,description="The length of time until a loan is due")
    month_or_year:LoanDurationType=Field(...,description="Term in year or month")