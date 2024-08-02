from unittest import TestCase, main
from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Test", 10)
        self.restaurant2 = Restaurant("Test2", 5)
        self.restaurant2.waiters = [
            {'name': 'Test1', 'total_earnings': 10},
            {'name': 'Test2', 'total_earnings': 20},
            {'name': 'Test3', 'total_earnings': 30},
        ]

    def test_correct_init(self):
        restaurant2_expected_result = [
            {'name': 'Test1', 'total_earnings': 10},
            {'name': 'Test2', 'total_earnings': 20},
            {'name': 'Test3', 'total_earnings': 30}
        ]

        self.assertEqual("Test", self.restaurant.name)
        self.assertEqual(10, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

        self.assertEqual("Test2", self.restaurant2.name)
        self.assertEqual(5, self.restaurant2.capacity)
        self.assertEqual(restaurant2_expected_result, self.restaurant2.waiters)

    def test_name_setter_raises_value_error_with_incorrect_name(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.name = ""
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_capacity_setter_raises_value_error_with_incorrect_capacity(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.capacity = -1
        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_get_waiters_filters_waiters_by_min_and_max_earnings(self):
        result = self.restaurant2.get_waiters(min_earnings=15, max_earnings=25)
        self.assertEqual([{'name': 'Test2', 'total_earnings': 20}], result)

    def test_add_waiter_returns_correct_message_when_there_are_no_more_places(self):
        self.restaurant.capacity = 1
        self.restaurant.waiters = [{'name': 'Test', 'total_earnings': 20}]

        result = self.restaurant.add_waiter("Test")
        self.assertEqual("No more places!", result)

    def test_add_waiter_returns_correct_string_if_waiter_already_exists(self):
        result = self.restaurant2.add_waiter("Test1")
        self.assertEqual("The waiter Test1 already exists!", result)

    def test_add_waiter_correctly_adds_new_waiter(self):
        result = self.restaurant2.add_waiter("Test4")
        expected_result = [
            {'name': 'Test1', 'total_earnings': 10},
            {'name': 'Test2', 'total_earnings': 20},
            {'name': 'Test3', 'total_earnings': 30},
            {'name': 'Test4'}
        ]
        self.assertEqual("The waiter Test4 has been added.", result)
        self.assertEqual(expected_result, self.restaurant2.waiters)

    def test_remove_waiter_removes_correct_waiter(self):
        result = self.restaurant2.remove_waiter("Test1")
        expected_result = [
            {'name': 'Test2', 'total_earnings': 20},
            {'name': 'Test3', 'total_earnings': 30}
        ]
        self.assertEqual("The waiter Test1 has been removed.", result)
        self.assertEqual(expected_result, self.restaurant2.waiters)

    def test_remove_waiter_returns_correct_message_if_waiter_does_not_exist(self):
        result = self.restaurant2.remove_waiter("Test")
        self.assertEqual("No waiter found with the name Test.", result)

    def test_get_total_earnings_returns_correct_total_earnings(self):
        result = self.restaurant2.get_total_earnings()
        self.assertEqual(60, result)

    def test_get_total_earnings_returns_zero_if_no_waiters(self):
        result = self.restaurant.get_total_earnings()
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
