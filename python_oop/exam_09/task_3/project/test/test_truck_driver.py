from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Pesho", 10)

    def test_init(self):
        self.assertEqual(self.driver.name, "Pesho")
        self.assertEqual(self.driver.money_per_mile, 10)
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)
        self.assertEqual(self.driver.available_cargos, {})

    def test_earned_money_setter_raises_value_error_if_earned_money_is_negative(self):
        expected_message = f"{self.driver.name} went bankrupt."

        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -10
        self.assertEqual(expected_message, str(ve.exception))
        self.assertEqual(0, self.driver.earned_money)

    def test_add_cargo_offer_correctly_adds_cargo_offer(self):
        expected_message = "Cargo for 10 to Sofia was added as an offer."

        actual_message = self.driver.add_cargo_offer("Sofia", 10)

        self.assertEqual(expected_message, actual_message)
        self.assertEqual({"Sofia": 10}, self.driver.available_cargos)

    def test_add_cargo_offer_raises_exception_if_cargo_offer_is_already_added(self):
        self.driver.add_cargo_offer("Sofia", 10)
        expected_message = "Cargo offer is already added."

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 10)

        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({"Sofia": 10}, self.driver.available_cargos)

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Sofia", 10)
        self.driver.add_cargo_offer("Varna", 20)
        self.driver.add_cargo_offer("Plovdiv", 30)

        expected_message = "Pesho is driving 30 to Plovdiv."

        actual_message = self.driver.drive_best_cargo_offer()

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(300, self.driver.earned_money)
        self.assertEqual(30, self.driver.miles)
        self.assertEqual(
            {"Sofia": 10, "Varna": 20, "Plovdiv": 30}, self.driver.available_cargos
        )

    def test_drive_best_cargo_offer_returns_correct_string_if_there_are_no_offers(self):
        expected_message = "There are no offers available."

        actual_message = self.driver.drive_best_cargo_offer()

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.assertEqual({}, self.driver.available_cargos)

    def test_check_for_activities_correctly_checks_for_activities(self):
        self.driver.add_cargo_offer("Seoul", 10000)

        expected_message = "Pesho is driving 10000 to Seoul."

        actual_message = self.driver.drive_best_cargo_offer()

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(88250, self.driver.earned_money)
        self.assertEqual(10000, self.driver.miles)
        self.assertEqual({"Seoul": 10000}, self.driver.available_cargos)

    def test_repr(self):
        expected = "Pesho has 0 miles behind his back."
        actual = self.driver.__repr__()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
