from app.schemas.loan_schema import Loan,LoanSchema
from app.services.file_service import read_db

def get_sum_of_principal_amount(loans=None):
    if loans == None:
        loans=read_db()
    total=sum([i['principal_amount'] for i in loans])
    return total

def get_sum_of_interest_amount(loans=None):
    if loans == None:
        loans=read_db()
    total=sum([i['total_interest'] for i in loans])
    return total

def get_sum_of_final_amount(loans=None):
    if loans == None:
        loans=read_db()
    total=sum([i['final_amount'] for i in loans])
    return total

def method1():
    pass

def method2():
    pass

def method3():
    pass

def method4():
    pass