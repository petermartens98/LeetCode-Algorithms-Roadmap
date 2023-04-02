class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concats = []
        l, r = 0, len(nums)-1
        while l<r:
            concats.append(int(str(nums[l]) + str(nums[r])))
            l+=1
            r-=1
        if len(nums)%2!=0: concats.append(nums[len(nums)//2])
        return sum(concats)
