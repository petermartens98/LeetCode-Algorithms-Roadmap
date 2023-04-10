class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [0] * len(s.split(" "))
        for i in s.split(" "):
            res[int(i[-1])-1] = i[:-1]
        return " ".join(i for i in res)
