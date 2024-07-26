from unittest import TestCase, main
# from worker.worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("TestPerson", 1000, 100)

    def test_correct_init(self):
        self.assertEqual("TestPerson", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_no_energy_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_when_worker_has_energy_decrease_energy_and_increase_money(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_increase_energy(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual(f'TestPerson has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
