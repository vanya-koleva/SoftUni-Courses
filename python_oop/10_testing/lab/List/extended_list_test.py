from unittest import TestCase, main
# from List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.int_list = IntegerList("a", 1, 2, 3, 4.4)

    def test_correct_init_ignores_non_integers(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_non_int_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add("add")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_int_is_added_to_the_list(self):
        expected_result = [1, 2, 3, 4]

        self.int_list.add(4)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_remove_index_with_invalid_index_raise_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_removes_valid_index(self):
        expected_result = [1, 3]

        self.int_list.remove_index(1)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_get_with_out_of_range_index_raise_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_when_index_is_in_range_returns_correct_value(self):
        self.assertEqual(2, self.int_list.get(1))

    def test_insert_on_invalid_index_raise_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(4, 4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_integer_on_valid_index_raises_a_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, "a")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_integer_on_valid_index(self):
        expected_result = self.int_list.get_data()
        expected_result.insert(1, 5)

        self.int_list.insert(1, 5)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_get_biggest_returns_biggest_int(self):
        result = self.int_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.int_list.get_index(2)

        self.assertEqual(1, result)


if __name__ == '__main__':
    main()
