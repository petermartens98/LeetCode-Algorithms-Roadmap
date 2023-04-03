class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # Solution 1
        '''
        diffs = {}
        for i, numi in enumerate(nums):
            for j in nums[i+1:]:
                diffs[abs(numi-j)] = 1 + diffs.get(abs(numi-j),0)
        return diffs.get(k,0)
        '''
        # Solution 2
        '''
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count = count + 1
        return count
        '''
        # Solution 3
        '''
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                counter += seen[tmp]
            if tmp2 in seen:
                counter += seen[tmp2]
            seen[num] += 1
        return counter
        '''
        # Solution 4
        seen = defaultdict(int)
        res = 0
        for num in nums:
            res += seen[num-k] + seen[num+k]
            seen[num] += 1
        return res
