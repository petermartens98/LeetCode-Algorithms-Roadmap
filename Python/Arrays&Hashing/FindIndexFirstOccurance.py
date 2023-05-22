class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i, char in enumerate(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
                
