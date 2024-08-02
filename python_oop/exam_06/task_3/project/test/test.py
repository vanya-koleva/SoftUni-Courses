from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('Porsche', 'sport', 1000, 10000.0)
        self.car2 = SecondHandCar('BMW', 'some_type', 1000, 9000.0)

    def test_correct_init(self):
        self.assertEqual(self.car.model, 'Porsche')
        self.assertEqual(self.car.car_type, 'sport')
        self.assertEqual(self.car.mileage, 1000)
        self.assertEqual(self.car.price, 10000.0)
        self.assertEqual(self.car.repairs, [])

    def test_setter_for_price_raises_value_error_if_price_is_equal_or_less_than_one(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_setter_for_mileage_raises_value_error_if_mileage_is_equal_or_less_than_100(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_set_promotional_price_raises_value_error_if_new_price_is_equal_or_greater_than_current_price(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(1000000.0)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price_correctly_sets_new_price(self):
        result = self.car.set_promotional_price(5000.0)

        self.assertEqual(self.car.price, 5000.0)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_returns_correct_message_if_repair_price_is_greater_than_half_of_car_price(self):
        result = self.car.need_repair(7000.0, 'broken wheel')
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_returns_correct_message_if_repair_price_is_less_than_half_of_car_price(self):
        expected_price = self.car.price + 3000.0
        epected_repairs = self.car.repairs + ['broken wheel']

        result = self.car.need_repair(3000.0, 'broken wheel')

        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(expected_price, self.car.price)
        self.assertEqual(epected_repairs, self.car.repairs)

    def test___gt__returns_correct_string_if_cars_are_different_types(self):
        result = self.car > self.car2
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test___gt__returns_correct_bool_if_cars_are_same_type(self):
        self.car2.car_type = 'sport'

        result = self.car > self.car2

        self.assertTrue(result)

    def test___str__returns_correct_string(self):
        self.assertEqual('Model Porsche | Type sport | Milage 1000km\nCurrent price: 10000.00 | Number of Repairs: 0', str(self.car))


if __name__ == '__main__':
    main()
