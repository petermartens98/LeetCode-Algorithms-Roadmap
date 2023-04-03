class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = 0 
        allowed = set(allowed)
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed:
                    consistent = False
                    break
            if consistent:
                res+=1
        return res
