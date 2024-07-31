from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Station")

    def test_correct_init(self):
        self.assertEqual("Station", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_incorrect_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            RailwayStation("")
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_short_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            RailwayStation("a")
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arrival_on_board_correctly_appends_info(self):
        self.station.new_arrival_on_board("Train")
        self.assertEqual(deque(['Train']), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_arrived_returns_correct_message_if_train_info_is_not_first_in_queue(self):
        self.station.arrival_trains.append("Train")
        self.station.arrival_trains.append("Train2")

        result = self.station.train_has_arrived("Train2")

        self.assertEqual(f"There are other trains to arrive before Train1.", result)
        self.assertEqual(deque(["Train", "Train2"]), self.station.arrival_trains)

    def test_train_has_arrived_returns_correct_message_if_train_info_is_first_in_queue(self):
        self.station.arrival_trains.append("Train")
        self.station.arrival_trains.append("Train2")

        result = self.station.train_has_arrived("Train")

        self.assertEqual(f"Train is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(["Train2"]), self.station.arrival_trains)
        self.assertEqual(deque(["Train"]), self.station.departure_trains)

    def test_train_has_arrived_returns_correct_message_if_train_info_is_not_in_queue(self):
        self.station.arrival_trains.append("Train")
        self.station.arrival_trains.append("Train2")

        result = self.station.train_has_arrived("Train3")

        self.assertEqual(f"There are other trains to arrive before Train3.", result)
        self.assertEqual(deque(["Train", "Train2"]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_left_returns_true_if_train_info_is_first_in_queue(self):
        self.station.departure_trains.append("Train")

        result = self.station.train_has_left("Train")

        self.assertEqual(True, result)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_left_returns_false_if_train_info_is_not_first_in_queue(self):
        self.station.departure_trains.append("Train")

        result = self.station.train_has_left("Train2")

        self.assertEqual(False, result)
        self.assertEqual(deque(["Train"]), self.station.departure_trains)
