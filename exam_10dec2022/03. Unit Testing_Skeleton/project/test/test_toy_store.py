from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.ts = ToyStore()

    def test_init(self):
        self.assertDictEqual(self.ts.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_successfully(self):
        result = self.ts.add_toy('A', 'Test')
        self.assertEqual(result, 'Toy:Test placed successfully!')

    def test_add_toy_if_shelf_not_in_keys_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy('Z', 'Test')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_if_already_in_shelf_raises_exception(self):
        self.ts.add_toy('A', 'Test')
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy('A', 'Test')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_if_shelf_is_already_taken_raises_exception(self):
        self.ts.add_toy('A', 'Test')
        with self.assertRaises(Exception) as ex:
            self.ts.add_toy('A', "Robot")
        self.assertEqual(str(ex.exception), 'Shelf is already taken!')

    def test_remove_toy_if_shelf_does_not_exist_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy('Z', 'Robot')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_if_toy_name_not_in_shelf(self):
        self.ts.add_toy('A', 'Test')
        with self.assertRaises(Exception) as ex:
            self.ts.remove_toy('A', 'Robot')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.ts.add_toy('A', 'Test')
        result = self.ts.remove_toy('A', 'Test')
        self.assertEqual(result, 'Remove toy:Test successfully!')
        self.assertIsNone(self.ts.toy_shelf['A'])

if __name__ == "__main__":
    main()