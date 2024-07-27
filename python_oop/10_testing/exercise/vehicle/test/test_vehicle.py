from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 100.00)

    def test_correct_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
        self.assertEqual(100.00, self.vehicle.horse_power)

    def test_drive_correctly_consumes_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_correctly_adds_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)

        self.assertEqual(10, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        self.assertEqual("The vehicle has 100.0 horse power with 50 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()
