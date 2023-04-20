class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        nums = sorted(nums)
        res = 0
        for i in range(1, len(nums)):
            res = max(res,(nums[i]-nums[i-1]))
        return res
