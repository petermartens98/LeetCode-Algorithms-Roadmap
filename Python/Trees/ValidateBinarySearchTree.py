# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid_bst_node(node: TreeNode, min_val: float, max_val: float) -> bool:
            if node is None: 
                return True
            if not (min_val < node.val < max_val): 
                return False
            return is_valid_bst_node(node.left, min_val, node.val) and \
                   is_valid_bst_node(node.right, node.val, max_val)

        return is_valid_bst_node(root, float('-inf'), float('inf'))
