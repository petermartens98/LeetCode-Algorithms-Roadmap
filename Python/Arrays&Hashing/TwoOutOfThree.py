class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        count = {}
        allnums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        for n in allnums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            if c>=2: res.append(n)
        return res
