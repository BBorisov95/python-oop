from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, fuel: int, horse_power: int):
        super().__init__(fuel=fuel, horse_power=horse_power)
