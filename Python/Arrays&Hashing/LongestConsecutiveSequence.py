class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        '''
        if len(nums)<2:
            return len(nums)
        temp = res = 1
        nums = sorted(set(nums))
        for i, numi in enumerate(nums[:-1:]):
            if numi + 1 == nums[i+1]:
                temp+=1
            else:
                temp=1
            if temp > res:
                res = temp
        return res
        '''
        # Solution 2
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
