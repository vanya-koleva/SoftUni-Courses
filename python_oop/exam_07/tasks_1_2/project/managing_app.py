from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {"CargoVan": CargoVan, "PassengerCar": PassengerCar}

    def __init__(self):
        self.users: List[User] = []
        self.routes: List[Route] = []
        self.vehicles: List[BaseVehicle] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            new_vehicle = self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        try:
            greater_length_route = [x for x in self.routes
                                    if x.start_point == start_point and
                                    x.end_point == end_point and
                                    x.length > length][0]

            greater_length_route.is_locked = True
        except IndexError:
            pass

        try:
            same_route = [x for x in self.routes if x.start_point == start_point and x.end_point == end_point and x.length == length][0]
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        except IndexError:
            try:
                lesser_length_route = [x for x in self.routes
                                       if x.start_point == start_point and
                                       x.end_point == end_point and
                                       x.length < length][0]

                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            except IndexError:
                new_route = Route(start_point, end_point, length, route_id)
                self.routes.append(new_route)
                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [x for x in self.vehicles if x.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))

        if len(sorted_vehicles) > count:
            sorted_vehicles = sorted_vehicles[:count]

        for vehicle in sorted_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        users = sorted(self.users, key=lambda x: -x.rating)

        message = ["*** E-Drive-Rent ***"]

        for user in users:
            message.append(str(user))

        return "\n".join(message)
