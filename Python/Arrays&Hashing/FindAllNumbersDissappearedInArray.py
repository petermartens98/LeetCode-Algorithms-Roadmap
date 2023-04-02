class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Solution 1 - Logically Worked, BUT Time Limit Exceeded
        '''
        res = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
        '''
        # Solution 2
        return list(set(range(1,len(nums)+1))-set(nums))
