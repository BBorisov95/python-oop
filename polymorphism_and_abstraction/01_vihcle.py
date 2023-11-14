from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, amount: float) -> None:
        pass


class Car(Vehicle):
    air_cond_fuel_consumption = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Car.air_cond_fuel_consumption)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += amount


class Truck(Vehicle):

    air_cond_fuel_consumption = 1.6
    holes_in_the_tank = 0.95

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Truck.air_cond_fuel_consumption)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += amount * Truck.holes_in_the_tank
