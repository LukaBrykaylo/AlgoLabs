import unittest
from src.cow_placement import cow_placement

class TestCowPlacement(unittest.TestCase):
    def test_example_case(self):
        n = 5
        c = 3
        free_sections = [1, 2, 8, 4, 9]
        result = cow_placement(n, c, free_sections)
        self.assertEqual(result, 3)

    def test_minimum_input(self):
        n = 2
        c = 2
        free_sections = [0, 1]
        result = cow_placement(n, c, free_sections)
        self.assertEqual(result, 1)

    def test_n_less_than_c(self):
        n = 3
        c = 4
        free_sections = [1, 3, 5]
        result = cow_placement(n, c, free_sections)
        self.assertEqual(result, 0)
