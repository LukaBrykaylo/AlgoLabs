import unittest

from src.diameter_binary_tree import BinaryTree, binary_tree_diameter

root = BinaryTree(3) 
root.right = BinaryTree(9)                              
root.right.right = BinaryTree(20) 
root.right.left = BinaryTree(7) 
root.right.left.right = BinaryTree(8) 
root.right.right.left = BinaryTree(15) 
root.right.right.left.right = BinaryTree(16) 

class DiameterBinaryTreeTest(unittest.TestCase):
    def test_case1(self):
        result = binary_tree_diameter(root)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()