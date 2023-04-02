class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Solution 1
        '''
        wealths = []
        for i in accounts:
            wealths.append(sum(i))
        return max(wealths)
        '''
        # Solution 2
        return max([sum(i) for i in accounts])
