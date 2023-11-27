import unittest
from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(35.5, 135)

    def test_correct_init(self):
        self.assertEqual(35.5, self.vehicle.fuel)
        self.assertEqual(135, self.vehicle.horse_power)
        self.assertEqual(35.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_correct_class_methods(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        # self.assertIsInstance(float, Vehicle.fuel_consumption)
        # self.assertIsInstance(float, Vehicle.fuel)
        # self.assertIsInstance(float, Vehicle.capacity)
        # self.assertIsInstance(float, Vehicle.horse_power)

    def test_drive_raises_exception_if_not_enough_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_enough_fuel_to_reduce_fuel(self):
        kilometers_to_drive = 10
        self.vehicle.drive(kilometers_to_drive)
        expected_left_fuel = 23
        self.assertEqual(expected_left_fuel, self.vehicle.fuel)

    def test_refuel_if_fuel_is_more_than_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(40)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_refiling_to_max_capacity_and_change_fuel_amount(self):
        self.vehicle.fuel = 20
        self.vehicle.refuel(15.5)
        self.assertEqual(35.5, self.vehicle.fuel)

    def test_class_str_dunder_method(self):
        expected_str = "The vehicle has 135 horse power with 35.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_str, self.vehicle.__str__())
