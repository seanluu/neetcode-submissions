class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0  # best area found so far, nothing checked yet

        # start at both ends, the widest possible container, then move inward
        l, r = 0, len(heights) - 1

        while l < r:
            # water is capped by the shorter bar, width is the distance between them
            # (r - l, not + 1, since we're measuring the gap, not counting elements)
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)  # keep the best area so far

            # move the shorter bar inward, since it's what limits the height
            # (moving the taller one only shrinks the width, it can't help)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res  # container with the most water

        # time: O(n), each pointer moves at most n times total
        # space: O(1), just two pointers