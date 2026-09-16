class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # height of the bars is determined by the lowest one
        # use two pointers since we care abt the beginning and end
        # and scanning til we get to the middle

        res = 0 # default output

        l, r = 0, len(heights) - 1 # first and last index

        # if they meet together at any point, we stop two pointers 
        while l < r:
            area = min(heights[l], heights[r]) * (r - l) # take min of height of the two bars, then the width
            res = max(res, area) # take best area we saw so far

            # if right bar is higher than the left
            if heights[l] < heights[r]:
                l += 1 # slide left bar closer to mid
            else: # if left bar is higher than right
                r -= 1 # slide right bar closer to mid
        return res # return final area

        # time complexity: O(n)
        # iterate through each height at least once

        # space complexity: O(1)
        # no crazy data structures used here