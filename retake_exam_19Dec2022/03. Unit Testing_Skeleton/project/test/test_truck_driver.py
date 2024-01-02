from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('Test', 3.5)

    def test_init(self):
        self.assertEqual(self.driver.name, 'Test')
        self.assertEqual(self.driver.money_per_mile, 3.5)
        self.assertDictEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_valid_setter(self):
        self.driver.earned_money = 10
        self.assertEqual(self.driver.earned_money, 10)
        self.driver.earned_money = 0
        self.assertEqual(self.driver.earned_money, 0)

    def test_earned_money_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -0.5
        self.assertEqual(str(ve.exception), f"Test went bankrupt.")

    def test_add_cargo_offer_successfully(self):
        result = self.driver.add_cargo_offer('Test_loc', 10)
        self.assertEqual(result, 'Cargo for 10 to Test_loc was added as an offer.')
        self.assertDictEqual(self.driver.available_cargos, {'Test_loc':10})

    def test_add_cargo_offer_location_already_added_raises_exception(self):
        self.driver.add_cargo_offer('Test_loc', 10)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Test_loc', 10)
        self.assertEqual(str(ex.exception), 'Cargo offer is already added.')

    def test_drive_best_cargo_offer_successfully(self):
        self.driver.add_cargo_offer('Test_loc', 10)
        self.driver.add_cargo_offer('Test_loc1', 9)
        self.assertDictEqual(self.driver.available_cargos, {'Test_loc': 10, 'Test_loc1': 9})
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.miles, 10)
        self.assertEqual(self.driver.earned_money, 35)
        self.assertEqual(result, f"Test is driving 10 to Test_loc.")

    def test_drive_best_cargo_fail(self):
        self.assertDictEqual(self.driver.available_cargos, {})
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, f"There are no offers available.")

    def test_check_for_activities(self):
        self.driver.add_cargo_offer('Test_loc', 10000)
        self.driver.drive_best_cargo_offer()
        self.driver.eat(10000)
        self.assertEqual(self.driver.earned_money, 23230.0)
        self.driver.sleep(10000)
        self.assertEqual(self.driver.earned_money, 23185.0)
        self.driver.pump_gas(10000)
        self.assertEqual(self.driver.earned_money, 23185.0)
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 15685.0)

    def test_repr(self):
        result = self.driver.__repr__()
        self.assertEqual(result, 'Test has 0 miles behind his back.')

+\
    main()
