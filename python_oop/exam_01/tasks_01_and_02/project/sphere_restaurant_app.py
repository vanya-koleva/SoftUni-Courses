from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    WAITER_TYPES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        if waiter_type not in self.WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = next(filter(lambda w: w.name == waiter_name, self.waiters), None)
        if waiter is not None:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."

        client = next(filter(lambda c: c.name == client_name, self.clients), None)
        if client is not None:
            return f"{client_name} is already a client."

        new_client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        waiter = next(filter(lambda w: w.name == waiter_name, self.waiters), None)

        if waiter is None:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client = next(filter(lambda c: c.name == client_name, self.clients), None)

        if client is None:
            return f"{client_name} is not a registered client."

        earned_points = client.earning_points(order_amount)

        return f"{client_name} earned {earned_points} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = next(filter(lambda c: c.name == client_name, self.clients), None)

        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        waiter_info = "** Waiter Details **\n"

        for waiter in sorted_waiters:
            waiter_info += str(waiter) + "\n"

        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        clients_count = len(self.clients)

        report = f"$$ Monthly Report $$\n" \
                 f"Total Earnings: ${total_earnings:.2f}\n" \
                 f"Total Clients Unused Points: {total_client_points}\n" \
                 f"Total Clients Count: {clients_count}\n"
        report += waiter_info

        return report.strip()
