from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player_1 = TennisPlayer("Pesho", 18, 10)
        self.player_2 = TennisPlayer("Gosho", 18, 0)

    def test_correct_init(self):
        self.assertEqual(self.player_1.name, "Pesho")
        self.assertEqual(self.player_1.age, 18)
        self.assertEqual(self.player_1.points, 10)

        self.assertEqual(self.player_2.name, "Gosho")
        self.assertEqual(self.player_2.age, 18)
        self.assertEqual(self.player_2.points, 0)

    def test_name_setter_raises_value_error_with_incorrect_name(self):
        with self.assertRaises(ValueError) as ex:
            self.player_1.name = ""
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.player_1.name = "Pe"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_age_setter_raises_value_error_with_incorrect_age(self):
        with self.assertRaises(ValueError) as ex:
            self.player_1.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

        with self.assertRaises(ValueError) as ex:
            self.player_1.age = 0
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_expect_success(self):
        self.player_1.add_new_win("First")
        self.assertEqual(["First"], self.player_1.wins)
        self.player_1.add_new_win("Second")
        self.assertEqual(["First", "Second"], self.player_1.wins)

    def test_add_new_win_when_tournament_already_added_returns_correct_message(self):
        self.player_1.add_new_win("First")
        expected_message = "First has been already added to the list of wins!"

        message = self.player_1.add_new_win("First")
        self.assertEqual(expected_message, message)
        self.assertEqual(["First"], self.player_1.wins)

    def test_lt_when_first_player_has_less_points_returns_correct_string(self):
        expected_message = f"{self.player_1.name} is a top seeded player and he/she is better than {self.player_2.name}"

        message = self.player_2 < self.player_1

        self.assertEqual(expected_message, message)

    def test_lt_when_first_player_has_more_points_returns_correct_string(self):
        expected_message = f"{self.player_1.name} is a better player than {self.player_2.name}"

        message = self.player_1 < self.player_2

        self.assertEqual(expected_message, message)

    def test_lt_method_returns_correct_string_with_gt_operator_when_first_player_has_more_points(self):
        expected_message = f"{self.player_1.name} is a top seeded player and he/she is better than {self.player_2.name}"

        message = self.player_1 > self.player_2

        self.assertEqual(expected_message, message)

    def test_lt_method_returns_correct_string_with_gt_operator_when_first_player_has_less_points(self):
        expected_message = f"{self.player_1.name} is a better player than {self.player_2.name}"

        message = self.player_2 > self.player_1

        self.assertEqual(expected_message, message)

    def test_str_returns_correct_string_when_player_has_no_wins(self):
        expected_string = f"Tennis Player: {self.player_1.name}\n" \
                          f"Age: {self.player_1.age}\n" \
                          f"Points: {self.player_1.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player_1.wins)}"

        string = str(self.player_1)

        self.assertEqual(expected_string, string)

    def test_str_returns_correct_string_when_player_has_wins(self):
        self.player_1.add_new_win("First")
        self.player_1.add_new_win("Second")

        expected_string = f"Tennis Player: {self.player_1.name}\n" \
                          f"Age: {self.player_1.age}\n" \
                          f"Points: {self.player_1.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player_1.wins)}"

        string = str(self.player_1)

        self.assertEqual(expected_string, string)


if __name__ == "__main__":
    main()
