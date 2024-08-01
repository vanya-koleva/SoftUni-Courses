from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(1000, 2, False)
        self.trip2 = Trip(1000, 1, True)
        self.trip3 = Trip(1_000_000, 2, True)

    def test_correct_init(self):
        self.assertEqual(1000, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(False, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

        self.assertEqual(1_000_000, self.trip3.budget)
        self.assertEqual(2, self.trip3.travelers)
        self.assertEqual(True, self.trip3.is_family)
        self.assertEqual({}, self.trip3.booked_destinations_paid_amounts)

    def test_travelers_setter_raises_a_value_error_if_travelers_is_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_is_family_setter_sets_to_false_if_travelers_is_one_person(self):
        self.assertFalse(self.trip2.is_family)

    def test_book_a_trip_returns_correct_string_if_destination_is_not_in_dictionary(self):
        result = self.trip.book_a_trip('Italy')
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_returns_correct_string_if_budget_is_not_enough(self):
        result = self.trip.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_returns_correct_string_if_destination_is_in_dictionary_and_budget_is_enough(self):
        result = self.trip.book_a_trip('Bulgaria')

        expected_budget = 0.00

        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is {self.trip.budget:.2f}', result)
        self.assertEqual(expected_budget, self.trip.budget)

    def test_book_a_trip_correctly_applies_family_discount(self):
        result = self.trip3.book_a_trip('Australia')

        expected_budget = 989740.0

        self.assertEqual(f'Successfully booked destination Australia! Your budget left is {self.trip3.budget:.2f}', result)
        self.assertEqual(expected_budget, self.trip3.budget)

    def test_booking_status_returns_correct_string_if_no_bookings(self):
        result = self.trip.booking_status()

        expected = 'No bookings yet. Budget: 1000.00'

        self.assertEqual(expected, result)

    def test_booking_status_returns_correct_string_when_booked(self):
        self.trip3.book_a_trip('New Zealand')
        result = self.trip3.booking_status()

        expected = (f'Booked Destination: New Zealand\n'
                    f'Paid Amount: 13500.00\n'
                    f'Number of Travelers: 2\n'
                    f'Budget Left: {self.trip3.budget:.2f}')

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
