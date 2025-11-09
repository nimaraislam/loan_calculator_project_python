import pytest
from app.schemas.loan_schema import Loan
def test_loan_interest_month():
    loan = Loan(2000,3,2)
    loan.calculate_loan_interest("M")

    assert loan.total_interest == 120.00

def test_loan_interest_year():
    loan =  Loan(2000,3,2)
    loan.calculate_loan_interest("Y")

    assert loan.total_interest == 1440.00

def test_loan_interest_invalid_month_or_year_option():
    expected_message="Use 'M' for months or 'Y' for years."
    loan =  Loan(2000,3,2)
    with pytest.raises(ValueError, match=expected_message):
        loan.calculate_loan_interest("Z")

    assert loan.total_interest == 0.00

def test_calculate_final_amount_month():
    loan =  Loan(2000,3,2)
    loan.calculate_loan_interest("M")

    assert loan.calculate_final_amount() == 2120.00

def test_calculate_final_amount_year():
    loan =  Loan(2000,3,2)
    loan.calculate_loan_interest("Y")

    assert loan.calculate_final_amount() == 3440.00

