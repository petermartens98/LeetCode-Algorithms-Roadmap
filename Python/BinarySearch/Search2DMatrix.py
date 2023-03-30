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
        '''
        allNums = []
        for i in matrix: allNums += i
        if target in allNums: return True
        return False
        '''

        # Solution 3
        '''
        for i in matrix:
            if target in i: return True
            if min(i)>target: break
        return False
        '''

        # Solution 4 - Binary Search
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
                
        if not (top <= bot):
            return False
        
        row = (top+bot)//2
        l, r = 0, COLS - 1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False


        
