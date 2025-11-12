import pytest
from app.schemas.loan_schema import Loan
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

#def test_loan_interest_invalid_month_or_year_option():
#    expected_message="Use 'M' for months or 'Y' for years."
#    loan =  Loan(2000,3,2,"Z")
#    with pytest.raises(ValueError, match=expected_message):
#        loan.calculate_loan_interest()

#    assert loan.total_interest == 0.00

