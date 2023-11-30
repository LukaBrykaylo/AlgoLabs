import unittest
from test.gas_management_test import GasManagementTest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(GasManagementTest)
    unittest.TextTestRunner().run(test_suite)
    