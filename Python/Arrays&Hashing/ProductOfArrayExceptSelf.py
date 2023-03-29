class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1 - Time Limit Exceeded
        '''
        res = []
        for i, numi in enumerate(nums):
            el = 1
            for j, numj in enumerate(nums):
                if i!=j:
                    el = el * numj
            res.append(el)
        return res
        '''
        # Solution 2
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
