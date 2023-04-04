class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Solution 1 - Brute Force
        '''
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        '''
        # Solution 2 - Binary Search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # Left Sorted Portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right Sorted Portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:  
                    l = mid + 1
        return -1
