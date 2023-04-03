class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Solution 1 - Time Limit Exceeded
        '''
        for i in sorted(nums1):
            for j in sorted(nums2):
                if i == j: return i
                elif j>i: break
        '''
        # Solution 2: - Two Pointers
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]: return nums1[i]
            elif nums1[i] < nums2[j]: i += 1
            else: j += 1
        return -1
