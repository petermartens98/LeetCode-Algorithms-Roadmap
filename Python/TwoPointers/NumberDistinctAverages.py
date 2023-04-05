class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs = []
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        while l <= r:
            avgs.append((nums[l]+nums[r])/2)
            l += 1
            r -= 1
        return len(set(avgs))
