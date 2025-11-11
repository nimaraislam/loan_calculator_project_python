from app.services.loan_service import *
from app.schemas.loan_schema import Loan
import pytest

def test_get_total_loan_number():
    loans = [{"principal_amount":1000},
             {"principal_amount":2000},
             {"principal_amount":7000},
             {"principal_amount":780},
             {"principal_amount":9000}]
    assert get_total_loan_number(loans)==5

def test_get_sum_of_principal_amount():
    loans = [{"principal_amount":1000},
             {"principal_amount":2000},
             {"principal_amount":7000}]
    assert get_sum_of_principal_amount(loans)==10000.00

def test_get_sum_of_interest_amount():
    loans = [{"total_interest":50.50},
             {"total_interest":20.00},
             {"total_interest":100}]
    assert get_sum_of_interest_amount(loans)==170.50

def test_get_sum_of_final_amount():
    loans = [{"final_amount":5000},
             {"final_amount":6000},
             {"final_amount":7700}]
    assert get_sum_of_final_amount(loans)==18700.00

def test_save_loan():
    loan=Loan(5500,4,3,"Y")
    loan.calculate_loan_interest()
    loan.calculate_final_amount()
    saved_loan = save_loan(loan)
    loans = read_db()
    assert saved_loan.id == 1
    assert len(loans) == 1
    assert loans[0]["principal_amount"] == 5500
    assert loans[0]["final_amount"] == saved_loan.final_amount


def test_calculate_monthly_installment():
    #monkeypatch
    assert calculate_monthly_installment(1) == 372.78

def test_get_loan_details_by_id():
   #monkeypatch
   loan = get_loan_details_by_id(1)
   assert loan["principal_amount"] == 5500
  


