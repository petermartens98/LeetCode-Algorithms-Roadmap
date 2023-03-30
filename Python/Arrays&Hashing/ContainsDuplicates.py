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
        # Solution 2
        '''
        return len(nums) != len(set(nums))
        '''
        # Solution 3
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
