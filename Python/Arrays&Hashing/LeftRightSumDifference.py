class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        # Solution 1
        '''
        lsum, rsum, res = [], [], []
        for i, _ in enumerate(nums):
            lsum.append(sum(nums[:i]))
            rsum.append(sum(nums[i+1:]))
            res.append(abs(lsum[i]-rsum[i]))
        return res
        '''
        # Solution 2
        res = []
        for i, _ in enumerate(nums):
            res.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return res
