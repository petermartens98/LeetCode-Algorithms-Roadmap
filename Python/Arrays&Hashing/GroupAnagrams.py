class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Solution 1
        '''
        res = defaultdict(list) # Mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
        '''
        # Solution 2
        '''
        res = defaultdict(list)
        for s in strs:
            res["".join(sorted(s))].append(s)
        return res.values()
        '''

                
