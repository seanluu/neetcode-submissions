class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area is determined by the height * width
        # we also notice that the height is determined by the lowest bar
        # on the left or right side... 

        # start at both ends, the widest possible container
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            # move the shorter bar, since it's what limits the height
            # (moving the taller one only shrinks the width, it can't help)
            if heights[l] < heights[r]:
                l += 1
            else:  # right bar is shorter or they're equal
                r -= 1
        return res

        # time: O(n), each pointer moves at most n times total
        # space: O(1)