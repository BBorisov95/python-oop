import unittest
from project.mammal import Mammal


class MammalTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Test_name', 'Human', 'Human_Sound')

    def test_correct_init_of_mammal_class(self):
        self.assertEqual('Test_name', self.mammal.name)
        self.assertEqual('Human', self.mammal.type)
        self.assertEqual('Human_Sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_to_make_human_sound(self):
        expected_sound = 'Test_name makes Human_Sound'
        result = self.mammal.make_sound()
        self.assertEqual(expected_sound, result)

    def test_get_mammal_kingdom_to_be_animals(self):
        expected_kingdom = 'animals'
        result = self.mammal.get_kingdom()
        self.assertEqual(expected_kingdom, result)

    def test_get_info_expected_to_be_result_name_and_type(self):
        expected_result = 'Test_name is of type Human'
        result = self.mammal.info()
        self.assertEqual(expected_result, result)
