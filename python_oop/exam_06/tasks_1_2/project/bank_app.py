from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans), None)
        client = next(filter(lambda c: c.client_id == client_id, self.clients), None)

        if loan_type != client.type_of_loan():
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients), None)

        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        affected_loans = [l for l in self.loans if l.__class__.__name__ == loan_type]

        for loan in affected_loans:
            loan.increase_interest_rate()

        return f"Successfully changed {len(affected_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = [c for c in self.clients if c.interest < min_rate]

        for client in affected_clients:
            client.increase_clients_interest()

        return f"Number of clients affected: {len(affected_clients)}."

    def get_statistics(self):
        total_clients_income = sum([c.income for c in self.clients])
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = sum([sum(l.amount for l in c.loans) for c in self.clients])

        if self.clients:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)
        else:
            avg_client_interest_rate = 0

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
