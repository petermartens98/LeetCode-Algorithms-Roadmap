class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Solution 1
        '''
        res = 0
        for i in operations:
            if '++' in i: res+=1
            if '--' in i: res-=1
        return res
        '''
        # Solution 2
        res = 0
        for i in operations:
            if '+' in i: res+=1
            else: res-=1
        return res
