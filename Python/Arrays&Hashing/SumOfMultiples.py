class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ''' Solution 1
        total_sum = 0
        for i in range(1, n+1):
            for j in [3,5,7]: 
                if i % j == 0: 
                    total_sum += i
                    break
        return total_sum
        '''
        # Solution 2
        '''
        total_sum = 0
        for i in range(3, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total_sum += i
        return total_sum
        '''
        # Solution 3
        return sum(i for i in range(3, n+1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)
