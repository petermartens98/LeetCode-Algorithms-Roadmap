class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Solution 1 - Time Limit Exceeded
        '''
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums):
                if i!=j and nums[i] == nums[j] and abs(i-j)<=k:
                    return True
        return False
        '''
        # Solution 2
        window = set()
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False        
