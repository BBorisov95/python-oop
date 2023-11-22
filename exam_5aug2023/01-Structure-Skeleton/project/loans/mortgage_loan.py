from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    RATE_INCREMENT = 0.5
    LOAN_TYPE = 'MortgageLoan'

    def __init__(self):
        super().__init__(3.5, 50_000.00)

    def increase_interest_rate(self, increase_amount: float = 0.5):
        self.interest_rate += self.RATE_INCREMENT
