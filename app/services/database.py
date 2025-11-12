from app.services.file_service import read_db,write_db,DB_PATH

class Database:

    def __init__(self,db_path=DB_PATH):
        self.db_path=db_path

    def save_loan(self,loan):
        loans = read_db(self.db_path)
        if len(loans) == 0:
            loan.id = len(loans) + 1
        else:
            loan.id = max([i['id'] for i in loans])+1
        loans.append(loan.to_dict())
        write_db(loans,self.db_path)
        loans=read_db()
        return loan
    
    def delete_loan_by_id(self,id):
        loans = read_db(self.db_path)
        loan_to_delete = next((i for i in loans if i["id"]==id),None)
        if loan_to_delete is None :
            return "Id does not exist." 
        else :
            loans.remove(loan_to_delete)
            write_db(loans,self.db_path)
            loans = read_db(self.db_path)
            return f"Loan with id {id} has been deleted."
        
    def calculate_monthly_installment(self,id):
        loans=read_db(self.db_path)
        loan = next((i for i in loans if i['id']== id),None)
        if not loan:
            return "Id does not exist."
        elif loan['month_or_year'] == "Y":
            return round((loan['final_amount']/(12*loan['term'])),2)
        elif loan['month_or_year'] == "M":
            return round((loan['final_amount']/loan['term']),2)
        
    def get_all_loans(self):
        loans = read_db(self.db_path)
        return loans
    
    def get_loan_details_by_id(self,id):
        loans = read_db(self.db_path)
        return next((i for i in loans if i['id']== id),None)

    def get_total_loan_number(self,loans=None):
        if loans == None:
            loans = read_db(self.db_path)
        return len(loans) 

    def get_sum_of_principal_amount(self,loans=None):
        if loans == None:
            loans=read_db(self.db_path)
        return sum([i['principal_amount'] for i in loans])

    def get_sum_of_interest_amount(self,loans=None):
        if loans == None:
            loans=read_db(self.db_path)
        return sum([i['total_interest'] for i in loans])

    def get_sum_of_final_amount(self,loans=None):
        if loans == None:
            loans=read_db(self.db_path)
        return sum([i['final_amount'] for i in loans])


    
   

    