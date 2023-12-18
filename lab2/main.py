import unittest
from test.cow_placement_test import TestCowPlacement

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestCowPlacement)
    unittest.TextTestRunner().run(test_suite)
