class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1 - Time Limit Exceeded
        '''
        for i, numi in enumerate(numbers):
            for j, numj in enumerate(numbers):
                if i != j:
                    if numi + numj == target:
                        return [i+1,j+1]
        ''' 
        # Solution 2
        l, r = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1, r+1]
        return
        
