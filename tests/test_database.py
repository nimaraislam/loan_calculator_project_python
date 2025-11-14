from app.services.database import Database
from app.services.loan_service import Loan
from app.services.file_service import read_db,write_db,TEST_DB_PATH
import pytest

test_database = Database(TEST_DB_PATH)

def test_save_loan():
    loan=Loan(5500,4,3,"Y")
    loan.calculate_loan_interest()
    loan.calculate_final_amount()
    saved_loan = test_database.save_loan(loan)
    loans = read_db(TEST_DB_PATH)
    assert saved_loan.id == 1
    assert len(loans) == 1
    assert loans[0]["principal_amount"] == 5500
    assert loans[0]["final_amount"] == saved_loan.final_amount

def test_delete_loan_by_id():
        pass
    

def test_get_loan_details_by_id():
   loan = test_database.get_loan_details_by_id(1)
   assert loan["id"] == 1

def test_calculate_monthly_installment():
    assert test_database.calculate_monthly_installment(1) == 372.78

def test_get_total_loan_number():
    loans = [{"principal_amount":1000},
             {"principal_amount":2000},
             {"principal_amount":7000},
             {"principal_amount":780},
             {"principal_amount":9000}]
    assert test_database.get_total_loan_number(loans)==5

def test_get_sum_of_principal_amount():
    loans = [{"principal_amount":1000},
             {"principal_amount":2000},
             {"principal_amount":7000}]
    assert test_database.get_sum_of_principal_amount(loans)==10000.00

def test_get_sum_of_interest_amount():
    loans = [{"total_interest":50.50},
             {"total_interest":20.00},
             {"total_interest":100}]
    assert test_database.get_sum_of_interest_amount(loans)==170.50

def test_get_sum_of_final_amount():
    loans = [{"final_amount":5000},
             {"final_amount":6000},
             {"final_amount":7700}]
    assert test_database.get_sum_of_final_amount(loans)==18700.00





  


