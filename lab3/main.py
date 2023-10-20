import unittest
from test.diameter_binary_tree_test import DiameterBinaryTreeTest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(DiameterBinaryTreeTest)
    unittest.TextTestRunner().run(test_suite)