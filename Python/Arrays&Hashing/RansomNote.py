class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomCounts = [0] * 26
        magCounts = [0] * 26
        
        # count characters in ransomNote
        for c in ransomNote:
            ransomCounts[ord(c) - ord('a')] += 1
        
        # count characters in magazine
        for c in magazine:
            magCounts[ord(c) - ord('a')] += 1
        
        # check if ransomNote can be constructed from magazine
        for i in range(26):
            if ransomCounts[i] > magCounts[i]:
                return False
        
        return True
