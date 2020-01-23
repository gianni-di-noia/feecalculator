"""Lendinvest unittest."""
import pytest

import config
from feecalculator import FeeCalculator, LoanApplication

PARAM1 = [(12, k, v,) for k, v in config.FEES[12].items()]
PARAM2 = [(24, k, v,) for k, v in config.FEES[24].items()]
PARAM3 = [(12, 1500, 70), (24, 1500, 85)]
PARAMS = PARAM1 + PARAM2 + PARAM3


@pytest.mark.parametrize("term,loan,expected", PARAMS)
def test_calculator(term, loan, expected):
    """Tests suite for fee calculator."""
    application = LoanApplication(term, loan)
    calculator = FeeCalculator(application)
    fee = calculator.calculate()
    assert fee == expected
