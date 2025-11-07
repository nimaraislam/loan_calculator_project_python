from typing import Optional
from pydantic import BaseModel, Field
class Loan:
    annaul_interest_rate = 3.00
    def __init__(self,principal_amount: float,term: int):
        if not isinstance(principal_amount,(int,float)):
            raise ValueError("Amount should be a number.")
        if principal_amount <= 0:
            raise ValueError("Amount should be greater than zero.")
        if not isinstance(term,int):
            raise ValueError("Term should be a number.")
        if term <= 0:
            raise ValueError("Term should be greater than zero.")
        
        self.id = 0
        self.principal_amount = principal_amount
        self.total_interest=0.00
        self.term=term
        self.final_amount = 0.00

    def calculate_loan_interest(self,month_or_year):
        if month_or_year == "M":
            self.total_interest =self.principal_amount*(self.annaul_interest_rate/100)*self.term
            return  self.total_interest
        elif month_or_year == "Y":
            self.total_interest =self.principal_amount*(self.annaul_interest_rate/100)*(self.term*12)
        else :
            raise ValueError("Use 'M' for months or 'Y' for years.")
        return  round(self.total_interest,2)
        
    def calculate_final_amount(self):
            self.final_amount = self.principal_amount + self.total_interest
            return round(self.final_amount,2)
        
    def to_dict(self):
        return {
            "id": self.id,
            "principal_amount" : self.principal_amount,
            "total_interest" : self.total_interest,
            "term" : self.term,
            "final_amount" : self.final_amount
        }


class LoanSchema(BaseModel):
    id:Optional[int] = Field(None,description= "Id of a customer.")
    principal_amount:float = Field(...,gt=0,description="Amount that customer wants to borrow.")
    interest:Optional[float]=Field(None,gt=0,description="Interest amount which customer needs to pay monthly")
    tenor:int=Field(...,gt=0,description="The length of time until a loan is due")