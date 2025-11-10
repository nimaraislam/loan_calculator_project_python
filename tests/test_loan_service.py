from app.services.loan_service import *
import pytest

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

