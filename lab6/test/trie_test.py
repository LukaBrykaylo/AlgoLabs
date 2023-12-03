import unittest

from src.trie import pattern_to_trie


class TrieTest(unittest.TestCase):
    def test_word_in_trie(self):
        patterns = ["cat", "dog", "apple", "cancel", "dom"]
        trie = pattern_to_trie(patterns)
        result = trie.search_word("cat")
        self.assertEqual(result, True)

    def test_prefix_in_trie(self):
        patterns = ["cat", "dog", "apple", "cancel", "dom"]
        trie = pattern_to_trie(patterns)
        result = trie.search_prefix("app")
        self.assertEqual(result, True) 

    def test_word_not_found(self):
        patterns = ["cat", "dog", "apple", "cancel", "dom"]
        trie = pattern_to_trie(patterns)
        result = trie.search_word("apply")
        self.assertEqual(result, "Not Found")

    def test_prefix_not_found(self):
        patterns = ["cat", "dog", "apple", "cancel", "dom"]
        trie = pattern_to_trie(patterns)
        result = trie.search_prefix("capp")
        self.assertEqual(result, "Not Found") 
    
if __name__ == "main":
    unittest.main()
