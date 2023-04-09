class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sCounts = [0] * 26
        tCounts = [0] * 26
        for c in s:
            sCounts[ord(c) - ord('a')] += 1
        for c in t:
            tCounts[ord(c) - ord('a')] += 1
        for i in range(26):
            if tCounts[i] > sCounts[i]:
                return chr(i + ord('a'))
