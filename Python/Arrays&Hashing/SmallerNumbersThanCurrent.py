class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Solution 1
        '''
        res = [0] * len(nums)
        for i, numi in enumerate(nums):
            for j in nums:
                if numi > j:
                    res[i] += 1
        return res
        '''
        # Solution 2
        sorted_nums = sorted(nums)
        mapping = dict()
        for i, n in enumerate(sorted_nums):
            if n not in mapping:
                mapping[n] = i
        
        return [mapping[key] for key in nums]
