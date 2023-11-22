from abc import ABC, abstractmethod


class BaseLoan(ABC):

    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self, increase_amount: float = 0.0):
        self.interest_rate += increase_amount
        return self.interest_rate
