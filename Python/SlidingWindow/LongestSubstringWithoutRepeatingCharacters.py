class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1
        if len(s) < 2: 
            return len(s)
        output = 1
        for i, chari in enumerate(s):
            chars = [chari]
            for j, charj in enumerate(s[i+1:]):
                if charj in chars: 
                    break
                else:
                    chars.append(charj)
                output = max(output, len(chars))
        return output
