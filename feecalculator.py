"""Fee Calculator module"""
import numpy as np

import config


class FeeCalculator:
    """
    The FeeCalculator object contains trances and investors as dictionaries.
    Parameters:
        applicatiom (LoanApplication): the LoanApplication obj
    """

    def __init__(self, application):
        self.loan = application.loan
        self.term = application.term

    def lower_bound(self) -> int:
        """Compute the lower bound for the given value."""
        bounds = sorted(config.FEES[self.term].keys(), reverse=True)
        for bound in bounds:
            if bound <= self.loan:
                return bound
        return bounds[0]

    def upper_bound(self) -> int:
        """Compute the upper bound for the given value."""
        bounds = sorted(config.FEES[self.term].keys())
        for bound in bounds:
            if bound >= self.loan:
                return bound
        return bounds[-1]

    def calculate(self) -> int:
        """Compute the fee.
        Returns:
            fee (int): the fee
        """
        lower = self.lower_bound()
        lower_fee = config.FEES[self.term][lower]
        upper = self.upper_bound()
        upper_fee = config.FEES[self.term][upper]
        fee = np.interp(self.loan, [lower, upper], [lower_fee, upper_fee])
        return fee


class LoanApplication:
    """
    The Loan object contains term and loan value.
    Parameters:
        term (int): the number of months the loan is on
        loan (int): the amount of pounds the loan is on
    """

    def __init__(self, term, loan):
        self.term = term
        self.loan = loan
