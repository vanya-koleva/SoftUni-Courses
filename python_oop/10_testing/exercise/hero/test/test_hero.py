from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("a", 1, 100.00, 100.00)
        self.enemy = Hero("b", 1, 50.00, 50.00)

    def test_init(self):
        self.assertEqual("a", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100.00, self.hero.health)
        self.assertEqual(100.00, self.hero.damage)

    def test_battle_with_same_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_lower_then_zero(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_lower_then_zero(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight b. He needs to rest", str(ex.exception))

    def test_battle_draw_returns_draw_and_decreases_health_on_both_players(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_battle_hero_wins_returns_correct_string_and_increases_hero_stats(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55.00, self.hero.health)
        self.assertEqual(105.00, self.hero.damage)

    def test_battle_enemy_wins_returns_correct_string_and_increases_enemy_stats(self):
        self.hero, self.enemy = self.enemy, self.hero
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct__str__(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
            f"Health: {self.hero.health}\n" \
            f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    main()
