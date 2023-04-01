class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ''' Solution 1
        count = 0
        for char in s[::-1].strip():
            if char == " ":
                break
            count = count + 1
        return count
        '''
        # Solution 2
        return len([i for i in s[::-1].strip().split()[0]])
