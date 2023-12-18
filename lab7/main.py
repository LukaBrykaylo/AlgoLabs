import unittest
from test.w_chain_test import WChainTest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(WChainTest)
    unittest.TextTestRunner().run(test_suite)
    