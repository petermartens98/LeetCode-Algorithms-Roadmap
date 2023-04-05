class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Solution 1 - Brute Force - Time Limit Exceeded
        '''
        if s == s[::-1]: return True
        for i,_ in enumerate(s):
            temp = (s[0:i]+s[i+1:])
            if temp == temp[::-1]: return True
        return False
        '''
        # Solution 2 - Two Pointers
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] 
                     or skipR == skipR[::-1])
            l, r = l+1, r-1
        return True
