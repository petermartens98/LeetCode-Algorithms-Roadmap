class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        '''
        zero_count = 0
        zero_indexes = []

        for i, num in enumerate(nums): 
            if num == 0:
                zero_indexes.append(i)
                zero_count += 1

        for i in sorted(zero_indexes, reverse=True):
            nums.pop(i)

        for i in range(zero_count):
            nums.append(0)
        '''
        # Solution 2 - Two Pointers
        '''
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
        ''' 
        # Solution 2 Condensed
        '''
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0 and nums[s] == 0: 
                nums[s], nums[f] = nums[f], nums[s]
            if nums[s] != 0: s += 1
        '''
        # Solution 2 - Further Improved
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0:
                if f != s: nums[s], nums[f] = nums[f], nums[s]
                s += 1
                
