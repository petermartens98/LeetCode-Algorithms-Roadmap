class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # Solution 1
        res = ""
        mapping = {}
        for c, i in zip(s, indices):
            mapping[i] = c
        for n, c in sorted(mapping.items()):
            res += c
        return res
