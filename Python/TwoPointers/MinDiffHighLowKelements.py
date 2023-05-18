class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ''' Solution 1
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])
        return min_diff
        '''
        # Solution 2
        '''
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
        '''
        # Solution 3
        nums.sort()
        l, r = 0, k - 1
        res = float("inf")
        
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res
