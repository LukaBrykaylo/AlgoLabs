class Node:
    def __init__(self):
        self.sub_nodes = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.sub_nodes:
                node.sub_nodes[char] = Node()
            node = node.sub_nodes[char]
        node.is_end = True 

    def search_word(self, word):
        node = self.root
        for char in word:
            if char not in node.sub_nodes:
                return 'Not Found'
            node = node.sub_nodes[char]
        return node.is_end
    
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.sub_nodes:
                return 'Not Found'
            node = node.sub_nodes[char]
        return True
    
def pattern_to_trie(patterns) -> Trie:
    trie = Trie()
    for pattern in patterns:
        trie.add(pattern)
    return trie
