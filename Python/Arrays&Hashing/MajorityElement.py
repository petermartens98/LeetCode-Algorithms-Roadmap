class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1
        '''
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        most = 0
        res = ""
        for n, c in counts.items():
            if c > most:
                most = c
                res = n
        return res
        '''
        # Solution 2
        '''
        counts, most, res = {}, 0, 0
        for n in nums: counts[n] = 1 + counts.get(n,0)
        for n, c in counts.items(): 
            if c > most: res, most = n, c
        return res
        '''
        # Solution 3
        '''
        counts = {}
        for n in nums: counts[n] = 1 + counts.get(n,0)
        return sorted(list(counts.items()), key=lambda x: x[1], reverse=True)[0][0]
        '''
        # Solution 4
        '''
        counts = {}
        for n in nums: counts[n] = counts.get(n, 0) + 1
        return sorted(counts, key=counts.get, reverse=True)[0]
        '''
        # Solution 5
        '''
        counts = {}
        for n in nums: counts[n] = counts.get(n, 0) + 1
        return max(counts, key=counts.get)
        '''
        # Solution 6
        '''
        counts = {n: nums.count(n) for n in set(nums)}
        return max(counts, key=counts.get)
        '''
        # Solution  7
        return max({n: nums.count(n) for n in set(nums)}, key={n: nums.count(n) for n in set(nums)}.get)
