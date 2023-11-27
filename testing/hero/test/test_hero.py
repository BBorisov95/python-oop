import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero('Test', 20, 100, 3)
        self.enemy = Hero('Enemy', 20, 100, 3)

    def test_correct_init(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(20, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(3, self.hero.damage)

    def test_battle_if_trying_to_fight_yourself_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_hero_health_is_zero_raises_ValueError(self):

        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_if_enemy_health_is_zero_raises_ValueError(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_if_hero_and_enemy_health_is_zero_return_draw_result(self):

        self.hero.health = 60
        self.enemy.health = 60
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_if_hero_has_bigger_damage_and_win_to_increase_level_health_and_damage_and_return_win_message(self):
        self.hero.damage = 5

        expected_level = 21
        expected_health = 45
        expected_damage = 10

        actual_result = self.hero.battle(self.enemy)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual("You win", actual_result)

    def test_battle_if_hero_lose_and_enemy_increase_health_and_damage_and_return_hero_lose_message(self):
        self.enemy.damage = 5

        expected_level = 21
        expected_health = 45
        expected_damage = 10

        actual_result = self.hero.battle(self.enemy)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)
        self.assertEqual("You lose", actual_result)

    def test_hero_string_dunder_method(self):
        expected = f"Hero Test: 20 lvl\nHealth: 100\nDamage: 3\n"
        actual_result = self.hero.__str__()
        self.assertEqual(expected, actual_result)

