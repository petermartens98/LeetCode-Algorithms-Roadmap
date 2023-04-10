# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1 - Recursive DFS
        '''
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''
        # Solution 2 - Iterative DFS
        '''
        res = 0
        stack =[[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
        '''
        # Solution 3 - BFS
        '''
        if not root: return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
        '''
        
