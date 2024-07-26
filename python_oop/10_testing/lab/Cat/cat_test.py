from unittest import TestCase, main

# from Cat.cat import Cat


class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Kitty")

    def test_correct_init(self):
        self.assertEqual("Kitty", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_is_fed_and_sleepy_and_size_increase_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_cat_eat_when_fed_raises_an_error(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_sleep_raise_an_error_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
