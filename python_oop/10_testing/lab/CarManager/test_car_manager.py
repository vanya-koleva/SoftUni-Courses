from unittest import TestCase, main

# from CarManager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Ferrari", "SF90 Stradale", 10, 100)

    def test_correct_init(self):
        self.assertEqual("Ferrari", self.car.make)
        self.assertEqual("SF90 Stradale", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_raises_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_negative_raises_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_int_raises_an_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_than_capacity_fills_to_capacity(self):
        self.car.refuel(1000)

        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_car_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_fuel_decreases_fuel_amount(self):
        self.car.refuel(100)
        self.car.drive(100)

        self.assertEqual(90, self.car.fuel_amount)


if __name__ == '__main__':
    main()
