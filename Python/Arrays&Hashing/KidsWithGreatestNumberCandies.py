class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Solution 1
        '''
        res = []
        for i in candies:
            if max(candies) <= i + extraCandies: res.append(True)
            else: res.append(False)
        return res
        '''
        # Solution 2
        '''
        maxCandies = max(candies)
        return [i + extraCandies >= maxCandies for i in candies]
        '''
        # Solution 3
        target = max(candies) - extraCandies
        return [i >= target for i in candies]
