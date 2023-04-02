class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Solution 1
        '''
        res = []
        for i in nums:
            res.append(nums[i])
        return res
        '''
        # Solution 2
        return [nums[i] for i in nums]
