class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Solution 1
        '''
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            width = right - left
            height = min(left_height, right_height)
            area = width * height
            if area > max_area:
                max_area = area

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area
        '''

        # Solution 2 : Condensed
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            lh, rh = heights[l], heights[r]
            w = r - l
            h = min(lh, rh)
            a = w * h
            res = max(res, a)
            if lh < rh: l+=1
            else: r-=1
        return res
