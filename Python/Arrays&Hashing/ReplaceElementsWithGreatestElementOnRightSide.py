class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = [-1]
        i=0
        while i < len(arr)-1:
            res.insert(i,max(arr[i+1:]))
            i+=1
        return res
