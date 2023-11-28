import unittest
from project.second_hand_car import SecondHandCar


class SecondHandCarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar('E90', 'Sedan', 125_000, 10_000)

    def test_init_if_correct(self):
        self.assertEqual('E90', self.car.model)
        self.assertEqual('Sedan', self.car.car_type)
        self.assertEqual(125_000, self.car.mileage)
        self.assertEqual(10_000, self.car.price)
        self.assertFalse(self.car.repairs)

    def test_setter_price_if_price_is_lower_than_one_to_raise_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_milage_setter_if_milage_is_lower_than_100_to_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 90

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_if_new_price_is_higher_to_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(11_000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_if_new_price_is_lower_to_set_new_price_and_return_message(self):
        expected_result = 'The promotional price has been successfully set.'
        actual_result = self.car.set_promotional_price(9_000)
        self.assertEqual(9_000, self.car.price)
        self.assertEqual(expected_result, actual_result)

    def test_need_repair_if_repair_price_is_bigger_then_the_half_of_the_car_price_to_return_message(self):
        expected_result = 'Repair is impossible!'
        actual_result = self.car.need_repair(7_000, 'new_engine')
        self.assertEqual(expected_result, actual_result)

    def test_need_repair_if_repair_price_is_lower_then_the_half_of_the_car_price_to_increment_car_price_and_add_rapair_description(self):
        expected_result = 'Price has been increased due to repair charges.'
        actual_result = self.car.need_repair(1_000, 'new brakes')
        self.assertEqual(11_000, self.car.price)
        self.assertEqual(expected_result, actual_result)

    def test_gt_dunder_method_return_message_if_incorrect_compare_type_is_set(self):
        expected_result = 'Cars cannot be compared. Type mismatch!'
        car_two = SecondHandCar('e91', 'combi', 135_000, 13_000)
        actual_result = self.car > car_two
        self.assertEqual(expected_result, actual_result)

    def test_gt_dunder_method_return_price_compare_if_car_types_are_correct(self):
        car_two = SecondHandCar('e91', 'Sedan', 135_000, 13_000)
        actual_result = self.car > car_two
        self.assertFalse(actual_result)

    def test_str_dunder_method_with_no_repairs(self):
        expected_result = """Model E90 | Type Sedan | Milage 125000km
Current price: 10000.00 | Number of Repairs: 0"""
        actual_result = self.car.__str__()
        self.assertEqual(expected_result, actual_result)

    def test_str_dunder_method_with_repairs(self):
        expected_result = """Model E90 | Type Sedan | Milage 125000km
Current price: 11000.00 | Number of Repairs: 1"""
        actual_result = self.car.need_repair(1_000, 'new brakes')
        actual_result = self.car.__str__()
        self.assertEqual(expected_result, actual_result)






