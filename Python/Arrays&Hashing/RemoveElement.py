class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Solution 1
        '''
        occ_indexes = []
        for i, num in enumerate(nums):
            if num == val:
                occ_indexes.append(i)

        for i in sorted(occ_indexes, reverse=True):
            nums.pop(i)

        return len(nums)
        '''
        # Solution 2
        '''
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
            else:
                nums[i-k] = nums[i]
        del nums[len(nums)-k:]
        return len(nums)
        '''
        # Solution 3
        '''
        i = 0
        while i < len(nums):
            if nums[i] == val: nums.pop(i)
            else: i += 1
        return len(nums)
        '''
        # Solution 4
        '''
        nums[:] = [num for num in nums if num != val]
        return len(nums)
        '''
        # Solution 5
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
