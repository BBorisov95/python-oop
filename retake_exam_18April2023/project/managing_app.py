from typing import List, Union
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.user import User
from project.route import Route


class ManagingApp:

    VALID_CAR_TYPES = {'PassengerCar': PassengerCar,
                       'CargoVan': CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[Union[CargoVan, PassengerCar]] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._get_user_by_driving_license_number(driving_license_number)
        if user:
            return f'{driving_license_number} has already been registered to our platform.'
        reg_user = User(first_name, last_name, driving_license_number)
        self.users.append(reg_user)
        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_CAR_TYPES:
            return f'Vehicle type {vehicle_type} is inaccessible.'
        vehicle = self._get_vehicle_by_register_plate_number(license_plate_number)
        if vehicle:
            return f'{license_plate_number} belongs to another vehicle.'
        vehicle_to_reg = self.VALID_CAR_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle_to_reg)
        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_to_find = self._check_if_route_exists(start_point, end_point)
        if route_to_find:
            if route_to_find.length == length:
                return f'{start_point}/{end_point} - {length} km had already been added to our platform.'
            if route_to_find.length < length:
                return f'{start_point}/{end_point} shorter route had already been added to our platform.'
            if route_to_find.length > length:
                route_to_find.is_locked = True
        route_to_reg = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(route_to_reg)
        return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._get_user_by_driving_license_number(driving_license_number)
        if user.is_blocked:
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'

        vehicle = self._get_vehicle_by_register_plate_number(license_plate_number)
        if vehicle.is_damaged:
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'

        route = self._get_route_by_id(route_id)
        if route.is_locked:
            return f'Route {route_id} is locked! This trip is not allowed.'

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        all_damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(all_damaged_vehicles, key=lambda x: (x.brand, x.model))
        for vehicle in sorted_vehicles[:count]:
            vehicle.recharge()
            vehicle.change_status()
        return f'{len(sorted_vehicles[:count])} vehicles were successfully repaired!'

    def users_report(self):
        result = ['*** E-Drive-Rent ***']
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        for u in sorted_users:
            result.append(str(u))
        return '\n'.join(result)

    def _get_user_by_driving_license_number(self, driving_license_number):
        searched_user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        return searched_user

    def _get_vehicle_by_register_plate_number(self, license_plate_number):
        searched_vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        return searched_vehicle

    def _check_if_route_exists(self, start_point, end_point):
        is_route = next((r for r in self.routes if r.start_point == start_point and
                         r.end_point == end_point), None)
        return is_route

    def _get_route_by_id(self, route_id):
        route = next((r for r in self.routes if r.route_id == route_id), None)
        return route