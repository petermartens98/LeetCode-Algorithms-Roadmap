class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        mid = len(nums)//2
        for i in range(0,n):
            res.append(nums[i])
            res.append(nums[mid+i])
        return res
