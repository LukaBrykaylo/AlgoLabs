class BinaryTree: 
    def __init__(self, value, left=None, right=None): 
        self.value = value 
        self.left = left 
        self.right = right 
 
def binary_tree_diameter(tree: BinaryTree) -> int: 
    result_diameter = [0]  
    path_number(tree, result_diameter) 
    return result_diameter[0] 
 
def path_number(tree, diameter): 
    if tree: 
        left_path = path_number(tree.left, diameter) 
        right_path = path_number(tree.right, diameter) 
        path = left_path + right_path 
        if path > diameter[0]: 
            diameter[0] = path 
        return max(left_path, right_path) + 1 
    return 0 
