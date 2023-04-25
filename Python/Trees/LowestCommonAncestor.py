# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Solution 1
        '''
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        '''
        # Solution 1 Condensed
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val: cur = cur.right
            elif p.val < cur.val and q.val < cur.val: cur = cur.left
            else: return cur
