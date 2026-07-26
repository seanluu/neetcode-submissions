class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # use sliding window here since we need the return the max amt of water
        # that a container can store, but this number changes frequently
        
        l, r = 0, len(heights) - 1 # use two pointers, first and last index

        res = 0 # since we want to return an integer

        while l < r:
            area = min(heights[l], heights[r]) * (r - l) # choose lowest height
            # then find the width using (r - l)
            res = max(res, area) # use max amt

            if heights[l] < heights[r]: 
                l += 1
            else:
                r -= 1
        return res 