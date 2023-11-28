import unittest
from project.tennis_player import TennisPlayer


class TennisPlayerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('Test-name', 18, 135.5)

    def test_if_correct_init(self):
        self.assertEqual('Test-name', self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(135.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_if_name_len_is_bellow_two_characters_raises_ValueError(self):

        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Te'
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_if_player_is_bellow_eighteen_raises_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_if_tournament_name_is_not_already_in_wins_adds_tournament_name_to_object_wins_attribute(self):
        t_name = 'Tournament for test'
        self.player.add_new_win(t_name)
        self.assertEqual(['Tournament for test'], self.player.wins)

    def test_add_new_win_if_tournament_is_already_in_wins_return_message(self):
        expected_result = 'Tournament for test has been already added to the list of wins!'
        self.player.add_new_win('Tournament for test')
        actual_result = self.player.add_new_win('Tournament for test')
        self.assertEqual(expected_result, actual_result)

    def test_lt_dunder_method_to_return_message_based_on_points(self):
        testing_char = TennisPlayer('Testing_name', 18, 140.00)
        expected_result_for_other_player_to_be_better = f'Testing_name is a top seeded player and he/she is better than Test-name'
        actual_result_for_other_player_to_be_better = self.player.__lt__(testing_char)
        self.assertEqual(expected_result_for_other_player_to_be_better, actual_result_for_other_player_to_be_better)

        testing_char.points = 120
        expected_result_for_player_to_be_better = f'Test-name is a better player than Testing_name'
        actual_result_for_player_to_be_better = self.player.__lt__(testing_char)
        self.assertEqual(expected_result_for_player_to_be_better, actual_result_for_player_to_be_better)

    def test_str_dunder_method(self):

        expected_result = f"Tennis Player: Test-name\n" \
               f"Age: 18\n" \
               f"Points: 135.5\n" \
               f"Tournaments won: "
        actual_result = str(self.player)
        self.assertEqual(expected_result, actual_result)

        self.player.wins = ['Tournament for test', 'Test2']
        expected_result_with_wins = f"Tennis Player: Test-name\n" \
                          f"Age: 18\n" \
                          f"Points: 135.5\n" \
                          f"Tournaments won: Tournament for test, Test2"
        self.assertEqual(expected_result_with_wins, str(self.player))

