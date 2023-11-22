from project.clients.base_client import BaseClient


class Adult(BaseClient):

    INTEREST_INCREMENT = 2
    ALLOWED_LOANS = 'MortgageLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 4.0)

    def increase_clients_interest(self, increase_interest=2.0):
        self.interest += self.INTEREST_INCREMENT

