import unittest

from src.w_chain import longest_chain
from src.w_chain import write_file


class WChainTest(unittest.TestCase):
    def test_without_first_last(self):
        write_file('lab7\src\wchain.in', '10\ncrates\ncar\ncats\ncrate\nrate\nat\nate\ntea\nrat\na')
        result = longest_chain()
        self.assertEqual(result, 6)

    def test_without_letters_between(self):
        write_file('lab7\src\wchain.in', '5\nb\nbcad\nbca\nbad\nbd\n')
        result = longest_chain()
        self.assertEqual(result, 4)
    
    def test_with_one_possible_result(self):
        write_file('lab7\src\wchain.in', '3\nword\nanotherword\nyetanotherword')
        result = longest_chain()
        self.assertEqual(result, 1)

if __name__ == "main":
    unittest.main()
