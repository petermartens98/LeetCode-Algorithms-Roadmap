class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Solution 1 - Time Limit Exceeded
        '''
        res = []
        for i, numi in enumerate(nums):
            temp=[]
            for j, numj in enumerate(nums):
                for k, numk in enumerate(nums):
                    if numi + numj + numk == 0:
                        if i != j and i != k and j != k:
                            if sorted([numi,numj,numk]) not in res:
                                res.append(sorted([numi,numj,numk]))
        return res
        '''
        # Solution 2 - Two Pointers
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
