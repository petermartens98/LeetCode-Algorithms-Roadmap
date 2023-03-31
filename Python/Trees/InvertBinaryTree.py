# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Depth First Search
        if not root: return None
        # Swap Children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # Recursive Call
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
