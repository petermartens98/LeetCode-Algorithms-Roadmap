class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1 ~ Brute Force ~ WC TC: O(n)
        '''
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums):
                if i != j and numi + numj == target:
                    return [min(i,j),max(i,j)]
        '''
        
        # Solution 2 - Hash Map
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
