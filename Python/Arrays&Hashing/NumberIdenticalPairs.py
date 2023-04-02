class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Solution 1
        '''
        res = 0
        for i, numi in enumerate(nums):
            for j in nums[i+1:]:
                if numi == j:
                    res+=1
        return res
        '''
        # Solution 2
        res = 0
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for n, count in counts.items():
            res += count * (count - 1) // 2
        return res
