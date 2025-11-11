from app.services.loan_service import Loan
from app.services.file_service import read_db,write_db

class Database:
    
    def get_total_loan_number(loans=None):
        if loans == None:
            loans = read_db()
        return len(loans) 

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

    def calculate_monthly_installment(loan_id):
        loans=read_db()
        loan = next((i for i in loans if i['id']== loan_id),None)
        if not loan:
            return "Id does not exist."
        elif loan['month_or_year'] == "Y":
            return round((loan['final_amount']/(12*loan['term'])),2)
        elif loan['month_or_year'] == "M":
            return round((loan['final_amount']/loan['term']),2)

    def get_loan_details_by_id(loan_id):
        loans = read_db()
        loan = next((i for i in loans if i['id']== loan_id),None)
        if not loan:
            return "Id does not exist."
        return loan

    def save_loan(loan):
        loans = read_db()
        if len(loans) == 0:
            loan.id = len(loans) + 1
        else:
            loan.id = max([i['id'] for i in loans])+1
        loans.append(loan.to_dict())
        write_db(loans)
        return loan