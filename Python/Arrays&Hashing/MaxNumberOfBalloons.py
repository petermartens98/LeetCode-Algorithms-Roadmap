class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Solution 1
        '''
        counts = {}
        for c in text:
            if c in "balloon":
                counts[c] = 1 + counts.get(c, 0)
        try:
            return min(counts['b'], counts['a'], counts['l']//2, counts['o']//2, counts['n'])
        except KeyError:
            return 0
        '''
        # Solution 1 Condensed
        '''
        counts = {}
        for c in text: 
            if c in "balloon": counts[c] = 1 + counts.get(c, 0)
        try: return min(counts['b'], counts['a'], counts['l']//2, counts['o']//2, counts['n'])
        except KeyError: return 0
        '''
        # Solution 2
        counts = {c: text.count(c) for c in "balloon"}
        return min(counts.get('b', 0), counts.get('a', 0), counts.get('l', 0) // 2, counts.get('o', 0) // 2, counts.get('n', 0))
