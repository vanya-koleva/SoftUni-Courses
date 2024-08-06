from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self) -> None:
        self.robot = Robot('123', 'Entertainment', 10, 1000)

        self.robot2 = Robot('124', 'Humanoids', 100, 2000)
        self.robot2.hardware_upgrades = ['Memory']
        self.robot2.software_updates = [2.0]

    def test_init(self):
        self.assertEqual('123', self.robot.robot_id)
        self.assertEqual('Entertainment', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

        self.assertEqual('124', self.robot2.robot_id)
        self.assertEqual('Humanoids', self.robot2.category)
        self.assertEqual(100, self.robot2.available_capacity)
        self.assertEqual(2000, self.robot2.price)
        self.assertEqual(['Memory'], self.robot2.hardware_upgrades)
        self.assertEqual([2.0], self.robot2.software_updates)

    def test_category_setter_returns_value_error_with_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Invalid'
        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_setter_returns_value_error_with_negative_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_returns_correct_string_if_hardware_already_exists(self):
        self.robot2.upgrade('Memory', 200)
        self.assertEqual(f"Robot {self.robot2.robot_id} was not upgraded.", self.robot2.upgrade('Memory', 200))
        self.assertEqual(2000, self.robot2.price)
        self.assertEqual(['Memory'], self.robot2.hardware_upgrades)

    def test_upgrade_with_new_hardware_expect_success(self):
        expected_price = self.robot.price + 200 * self.PRICE_INCREMENT

        result = self.robot.upgrade("CPU", 200)

        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with CPU.', result)
        self.assertEqual(expected_price, self.robot.price)
        self.assertEqual(["CPU"], self.robot.hardware_upgrades)

    def test_update_with_lower_version_returns_correct_string(self):
        result = self.robot2.update(1.0, 100)

        self.assertEqual(f"Robot {self.robot2.robot_id} was not updated.", result)
        self.assertEqual([2.0], self.robot2.software_updates)
        self.assertEqual(100, self.robot2.available_capacity)

    def test_update_with_same_version_returns_correct_string(self):
        result = self.robot2.update(2.0, 100)

        self.assertEqual(f"Robot {self.robot2.robot_id} was not updated.", result)
        self.assertEqual([2.0], self.robot2.software_updates)
        self.assertEqual(100, self.robot2.available_capacity)

    def test_update_when_capacity_is_insufficient(self):
        result = self.robot.update(2.0, 10000)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(10, self.robot.available_capacity)

    def test_update_expect_success(self):
        result = self.robot.update(2.0, 10)

        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 2.0.', result)
        self.assertEqual([2.0], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)

    def test_gt_returns_correct_string_with_less_than_operator_when_second_robot_is_more_expensive(self):
        result = self.robot < self.robot2
        self.assertEqual(f'Robot with ID {self.robot2.robot_id} is more expensive than Robot with ID {self.robot.robot_id}.', result)

    def test_gt_returns_correct_string_with_less_than_operator_when_first_robot_is_more_expensive(self):
        result = self.robot2 < self.robot
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.robot2.robot_id}.', result)

    def test_gt_returns_correct_string_when_second_robot_is_more_expensive(self):
        result = self.robot > self.robot2
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.robot2.robot_id}.', result)

    def test_gt_returns_correct_string_when_first_robot_is_more_expensive(self):
        result = self.robot2 > self.robot
        self.assertEqual(f'Robot with ID {self.robot2.robot_id} is more expensive than Robot with ID {self.robot.robot_id}.', result)

    def test_gt_returns_correct_string_with_equal_price(self):
        self.robot.price = self.robot2.price

        result = self.robot > self.robot2
        self.assertEqual(f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.robot2.robot_id}.', result)


if __name__ == '__main__':
    main()
