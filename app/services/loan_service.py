#from app.schemas.loan_schema import Loan,LoanSchema
from app.services.file_service import read_db,write_db
class Loan:
    #annaul_interest_rate = 3.00
    def __init__(self,principal_amount: float,interest_rate: float,term: int,month_or_year: str):
        if not isinstance(principal_amount,(int,float)):
            raise ValueError("Amount should be a number.")
        if principal_amount <= 0:
            raise ValueError("Amount should be greater than zero.")
        if not isinstance(interest_rate,(int,float)):
            raise ValueError("Interest rate should be a number.")
        if interest_rate <= 0:
            raise ValueError("Interest rate should be greater than zero.")
        if not isinstance(term,int):
            raise ValueError("Term should be a number.")
        if month_or_year.upper() not in ['M','Y']:
            raise ValueError("Duration must be specified as 'M' (Month) or 'Y' (Year).")
        if term <= 0:
            raise ValueError("Term should be greater than zero.")
        
        self.id = 0
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.term=term
        self.month_or_year = month_or_year.upper()
        self.total_interest=0.00
        self.final_amount = 0.00

    def calculate_loan_interest(self):
        if self.month_or_year == "M":
            self.total_interest =self.principal_amount*(self.interest_rate/100)*self.term
            return  self.total_interest
        elif self.month_or_year == "Y":
            self.total_interest =self.principal_amount*(self.interest_rate/100)*(self.term*12)
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
            "interest_rate" : self.interest_rate,
            "term" : self.term,
            "month_or_year" : self.month_or_year,
            "total_interest" : self.total_interest,
            "final_amount" : self.final_amount
        }
    
