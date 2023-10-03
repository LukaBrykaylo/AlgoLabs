import unittest

from longest_peak import longest_peak


class TestLongestPeak(unittest.TestCase):
    def test_1(self):
        numbers = [1, 2, 3, 4, 5, 6]
        self.assertEqual(longest_peak(numbers), 0)

    def test_2(self):
        numbers = [6, 5, 4, 3, 2, 1]
        self.assertEqual(longest_peak(numbers), 0)

    def test_3(self):
        numbers = [1, 2]
        self.assertEqual(longest_peak(numbers), 0)

    def test_4(self):
        numbers = [1, 1, 1, 1, 1, 1]
        self.assertEqual(longest_peak(numbers), 0)

    def test_5(self):
        numbers = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 5, 8, 10, 11, 0]
        self.assertEqual(longest_peak(numbers), 7)

    def test_6(self):
        numbers = [1, 3, 1, 8, 4, 2]
        self.assertEqual(longest_peak(numbers), 4)


if __name__ == "__main__":
    unittest.main()
