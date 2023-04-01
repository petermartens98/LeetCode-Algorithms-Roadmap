class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1
        i = j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
