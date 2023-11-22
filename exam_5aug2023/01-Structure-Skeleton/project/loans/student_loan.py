from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    RATE_INCREMENT = 0.2
    LOAN_TYPE = 'StudentLoan'

    def __init__(self):
        super().__init__(1.5, 2000.00)

    def increase_interest_rate(self, increase_amount=0.2):
        self.interest_rate += self.RATE_INCREMENT
