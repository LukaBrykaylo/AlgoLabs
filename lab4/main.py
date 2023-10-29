import unittest
from test.number_of_islands_test import NumberOfIslandsTest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(NumberOfIslandsTest)
    unittest.TextTestRunner().run(test_suite)
    