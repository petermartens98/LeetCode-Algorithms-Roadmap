class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for i, num in enumerate(nums):
            if leftSum == rightSum - leftSum - num: return i
            leftSum += num
        return -1
