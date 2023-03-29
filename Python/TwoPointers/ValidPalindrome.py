import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Solution 1: Regex Solution
        '''
        regex = re.compile('[^a-z0-9]')
        s = regex.sub('',s.lower())
        return s == s[::-1]
        '''
        # Solution 2
        '''
        new = ""
        for c in s:
            if c.isalnum():
                new += c.lower()
        return new == new[::-1]
        '''
        # Solution 3
        l, r = 0, len(s) - 1
        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while r>l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))ofl
