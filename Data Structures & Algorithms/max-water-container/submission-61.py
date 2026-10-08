class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area is determined by the height * width
        # we also notice that the height is determined by the lowest bar
        # on the left or right side... 

        # since we care about the left and right bars, we use two pointers

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
        
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res