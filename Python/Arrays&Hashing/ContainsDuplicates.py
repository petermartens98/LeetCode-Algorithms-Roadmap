class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ''' Solution Fails Time Limit
        seen = []
        for i in nums:
            if i in seen:
                return True
            seen.append(i)
        return False
        '''
        return len(nums) != len(set(nums))
