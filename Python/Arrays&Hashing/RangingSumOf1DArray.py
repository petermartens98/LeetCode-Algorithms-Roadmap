class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1:
        '''
        res = []
        for  i, _ in enumerate(nums):
            res.append(sum(nums[:i+1]))
        return res
        '''
        # Solution 2 - Solution 1 Condensed
        '''
        return [sum(nums[:i+1]) for i, _ in enumerate(nums)]
        '''
        # Solution 3
        ''' 
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
        '''
        # Solution 4
        return [sum(nums[:i+1]) for i in range(len(nums))]
        
