import unittest
from project.robot import Robot


class RobotTest(unittest.TestCase):

    def setUp(self):
        self.robot = Robot('RandomID', 'Military', 5, 135.5)

    def test_correct_init(self):
        self.assertEqual('RandomID', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(135.5, self.robot.price)
        self.assertFalse(self.robot.hardware_upgrades)
        self.assertFalse(self.robot.software_updates)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_category_setter_raises_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'TEST'

        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_price_setter_raises_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual('Price cannot be negative!', str(ve.exception))

    def test_upgrade_if_hardware_already_exist_return_msg_or_update_is_done_and_price_increased(self):
        expected_output_not_upgraded = 'Robot RandomID was not upgraded.'
        update_done = self.robot.upgrade('chip', 5)
        self.assertEqual('Robot RandomID was upgraded with chip.', update_done)
        self.assertEqual(143., self.robot.price)
        actual_output_not_upgraded = self.robot.upgrade('chip', 5)
        self.assertEqual(expected_output_not_upgraded, actual_output_not_upgraded)

    def test_update_if_software_update_version_is_lower_then_actual_version_or_robot_has_no_capacity_return_msg(self):
        expected_output = 'Robot RandomID was not updated.'
        self.robot.software_updates = [1,2,3,4,5]
        software_version_less_than_max = self.robot.update(3, 2)
        self.assertEqual(expected_output, software_version_less_than_max)
        software_capacity_not_enough = self.robot.update(6, 6)
        self.assertEqual(expected_output, software_capacity_not_enough)

    def test_update_successfully_append_version_to_list_and_decrease_capacity(self):
        expected_output = f'Robot RandomID was updated to version 7.'
        actual_output = self.robot.update(7, 3)
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(2, self.robot.available_capacity)

    def test_gt_dunder_method(self):
        other_robot = Robot('1', 'Military', 5, 120)
        expected_output_less_then = 'Robot with ID RandomID is more expensive than Robot with ID 1.'
        actual_output_for_robot_more_expensive_then_other_robot = self.robot > other_robot
        self.assertEqual(expected_output_less_then, actual_output_for_robot_more_expensive_then_other_robot)

        expected_output_equal = 'Robot with ID RandomID costs equal to Robot with ID 1.'
        other_robot.price = 135.5
        actual_equal = self.robot > other_robot
        self.assertEqual(expected_output_equal, actual_equal)

        expected_robot_cheaper_than_other = 'Robot with ID RandomID is cheaper than Robot with ID 1.'
        other_robot.price = 145.5
        actual_robot_cheaper_then_other = self.robot > other_robot
        self.assertEqual(expected_robot_cheaper_than_other, actual_robot_cheaper_then_other)