class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Solution 1 
        '''
        for i, numi in enumerate(arr):
            for j, numj in enumerate(arr):
                if i != j:
                    if numi == 2 * numj:
                        return True
        return False
        '''
        # Solution 2 - Binary Search Approach
        '''
        arr.sort()
        for i in range(len(arr)):
            product = arr[i]*2
            lo,hi = 0,len(arr)-1
            while lo<=hi:
                mid = (lo+hi)//2
                if arr[mid]==product and mid!= i:
                    return True
                elif arr[mid]<product:
                    lo+=1
                else:
                    hi-=1
        return False
        '''
        # Solution 3 - Hash Map Approach
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]]  = arr[:i]
            
        for key,val in dic.items():
            if 2*key in val:
                return True
            elif key%2==0 and key//2 in val:
                return True
