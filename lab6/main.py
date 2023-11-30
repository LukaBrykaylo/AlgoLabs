import unittest
from test.trie_test import TrieTest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TrieTest)
    unittest.TextTestRunner().run(test_suite)
    