import pytest
from app.services.loan_service import Loan
def test_loan_interest_month():
    loan = Loan(2000,3,2,"M")
    loan.calculate_loan_interest()

    assert loan.total_interest == 120.00

def test_loan_interest_year():
    loan =  Loan(2000,3,2,"Y")
    loan.calculate_loan_interest()

    assert loan.total_interest == 1440.00


def test_calculate_final_amount_month():
    loan =  Loan(2000,3,2,"M")
    loan.calculate_loan_interest()

    assert loan.calculate_final_amount() == 2120.00

def test_calculate_final_amount_year():
    loan =  Loan(2000,3,2,"Y")
    loan.calculate_loan_interest()

    assert loan.calculate_final_amount() == 3440.00


