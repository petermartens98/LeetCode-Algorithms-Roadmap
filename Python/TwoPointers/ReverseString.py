class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Solution 1
        '''
        for i,chari in enumerate(s):
            s.pop(i)
            s.insert(0,chari)
        '''
        # Solution 2
        '''
        s[:] = s[::-1]
        '''
        # Solution 3 - Two Pointers
        '''
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1; r -= 1
        '''
