from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("some name", "some type", "some sound")

    def test_correct_init(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_makes_sound_returns_correct_string(self):
        expected = "some name makes some sound"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom_returns_correct_string(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info_returns_correct_string(self):
        expected = "some name is of type some type"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
