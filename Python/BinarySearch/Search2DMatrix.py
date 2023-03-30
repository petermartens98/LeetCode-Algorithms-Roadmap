class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution 1
        '''
        for i in matrix:
            for j in i:
                if target == j:
                    return True
                elif j>target:
                    continue
        return False
        '''

        # Solution 2
        allNums = []
        for i in matrix:
            allNums += i
        allNums = sorted(allNums)
        if target in allNums:
            return True
        return False
