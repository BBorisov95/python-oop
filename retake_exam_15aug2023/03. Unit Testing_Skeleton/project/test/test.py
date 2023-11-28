import unittest
from project.trip import Trip


class TripTest(unittest.TestCase):

    def setUp(self) -> None:
        self.trip_one_guy_no_family = Trip(7500, 1, False)
        self.trip_two_persons_family = Trip(15000, 2, True)

    def test_class_method_if_each_country_is_correctly_set(self):
        expected_result = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}
        self.assertEqual(expected_result, Trip.DESTINATION_PRICES_PER_PERSON)

    def test_class_methods_if_each_country_has_right_price_for_travel(self):
        self.assertEqual(7500, Trip.DESTINATION_PRICES_PER_PERSON['New Zealand'])
        self.assertEqual(5700, Trip.DESTINATION_PRICES_PER_PERSON['Australia'])
        self.assertEqual(6200, Trip.DESTINATION_PRICES_PER_PERSON['Brazil'])
        self.assertEqual(500, Trip.DESTINATION_PRICES_PER_PERSON['Bulgaria'])

    def test_correct_initialisation_of_class_objects(self):
        self.assertEqual(7500, self.trip_one_guy_no_family.budget)
        self.assertEqual(1, self.trip_one_guy_no_family.travelers)
        self.assertFalse(self.trip_one_guy_no_family.is_family)
        self.assertTrue(self.trip_two_persons_family.is_family)
        self.assertEqual({},self.trip_one_guy_no_family.booked_destinations_paid_amounts)

    def test_if_travelers_are_below_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip_one_guy_no_family.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_if_family_is_set_only_if_travelers_are_more_or_equal_to_two_otherwise_set_it_to_false(self):
        self.trip_one_guy_no_family.is_family = True
        self.assertFalse(self.trip_one_guy_no_family.is_family)
        self.trip_one_guy_no_family.travelers = 2
        self.trip_one_guy_no_family.is_family = True
        self.assertTrue(self.trip_one_guy_no_family.is_family)

    def test_property_methods_getters_for_travelers_count_and_is_family(self):
        self.assertEqual(1, self.trip_one_guy_no_family.travelers)
        self.assertFalse(self.trip_one_guy_no_family.is_family)

    def test_book_a_trip_if_destination_not_in_class_methods_return_message(self):
        expected_result = 'This destination is not in our offers, please choose a new one!'
        actual_result = self.trip_one_guy_no_family.book_a_trip('Invalid Country')
        self.assertEqual(expected_result, actual_result)

    def test_book_a_trip_if_budged_is_not_enough_to_return_message(self):
        self.trip_one_guy_no_family.budget = 7400
        expected_result = 'Your budget is not enough!'
        actual_result = self.trip_one_guy_no_family.book_a_trip('New Zealand')
        self.assertEqual(expected_result, actual_result)

    def test_book_a_trip_if_budged_is_enough_to_return_message_and_reduce_budged(self):
        expected_result = 'Successfully booked destination New Zealand! Your budget left is 0.00'
        actual_result = self.trip_one_guy_no_family.book_a_trip('New Zealand')
        self.assertEqual(expected_result, actual_result)

    def test_booking_status_if_no_bookings_make_to_return_message(self):
        expected_result = 'No bookings yet. Budget: 7500.00'
        actual_result = self.trip_one_guy_no_family.booking_status()
        self.assertEqual(expected_result, actual_result)

    def test_booking_status_if_bookings_are_made_to_return_message_of_booked_destinations_and_paid_prices(self):
        expected_result = """Booked Destination: New Zealand
Paid Amount: 7500.00\nNumber of Travelers: 1
Budget Left: 0.00"""
        self.trip_one_guy_no_family.book_a_trip('New Zealand')
        actual_result = self.trip_one_guy_no_family.booking_status()
        self.assertEqual(expected_result, actual_result)

    def test_booking_status_if_family_and_bookings_are_made_to_return_message_of_booked_destinations_and_paid_prices(self):
        expected_result = """Booked Destination: New Zealand
Paid Amount: 13500.00\nNumber of Travelers: 2
Budget Left: 1500.00"""
        self.trip_two_persons_family.book_a_trip('New Zealand')
        actual_result = self.trip_two_persons_family.booking_status()
        self.assertEqual(expected_result, actual_result)