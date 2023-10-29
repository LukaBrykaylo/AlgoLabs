import unittest

from src.number_of_islands import number_of_islands

islands_map = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]


class NumberOfIslandsTest(unittest.TestCase):
    def test_case1(self):
        result = number_of_islands(islands_map)
        self.assertEqual(result, 5)

    def test_case2(self):
        islands_map = [
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        ]
        result = number_of_islands(islands_map)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
