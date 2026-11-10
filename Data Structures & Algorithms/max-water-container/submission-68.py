class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # return max amount of water that a container can store

        # in the picture, we see that we choose the bar with the lowest height

        # we start from the first index to the last index

        l, r = 0, len(heights) - 1

        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l) # take lowest bar height and multiply by the width
            res = max(res, area) # take best area we've seen so far

            # move the shorter bar; it's the one limiting the height,
            # moving the taller one can only shrink width without raising the min
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res

        # tc: O(n) since we iterate through each height once
        # sc: O(1), no crazy data structures used here just two pointers

