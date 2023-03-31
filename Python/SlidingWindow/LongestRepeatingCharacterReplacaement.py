class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Solution 1
        '''
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1) - (max(count.values())) > k:
                count[s[l]] -= l
                l += 1
            res = max(res, r-l+1)
        return res
        '''
        # Solution 2
        count = {}
        res = l = maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - maxf > k:
                count[s[l]] -= l
                l += 1
            res = max(res, r-l+1)
        return res
