from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation('Test')

    def test_init(self):
        self.assertEqual(self.station.name, 'Test')
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'te'

        self.assertEqual(str(ve.exception), 'Name should be more than 3 symbols!')

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board('ten')
        self.assertEqual(self.station.arrival_trains, deque(['ten']))

    def test_train_has_arrived_return_add_to_collection_or_remove_from_collection(self):
        self.station.new_arrival_on_board('ten')
        result = self.station.train_has_arrived('ten')
        self.assertEqual(result, 'ten is on the platform and will leave in 5 minutes.')
        self.assertEqual(self.station.arrival_trains, deque())

        self.station.new_arrival_on_board('ten')
        result = self.station.train_has_arrived('five')
        self.assertEqual(result, 'There are other trains to arrive before five.')
        self.assertEqual(self.station.arrival_trains, deque(['ten']))

    def test_train_has_left_and_pop(self):
        self.station.new_arrival_on_board('ten')
        self.station.train_has_arrived('ten')
        self.assertEqual(self.station.departure_trains, deque(['ten']))
        self.assertTrue(self.station.train_has_left('ten'))
        self.assertEqual(self.station.departure_trains, deque())

        self.station.new_arrival_on_board('ten')
        self.station.train_has_arrived('ten')
        self.assertFalse(self.station.train_has_left('five'))

if __name__ == "__main__":
    main()