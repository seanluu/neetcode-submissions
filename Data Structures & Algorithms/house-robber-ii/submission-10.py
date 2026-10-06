class Solution:

    # bottom-up dp
    def rob(self, nums: List[int]) -> int:
        # first and last house are neighbors, so either skip the first house
        # or skip the last house, and solve each as regular house robber
        # nums[0] handles the single house case (both slices would be empty)
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        # regular house robber on a straight line of houses
        # rob1 = best total up to two houses back, rob2 = best total up to the previous house
        rob1, rob2 = 0, 0  # no houses means no money

        for num in nums:
            # rob this house and add it to the best from two back, or skip it
            newRob = max(rob1 + num, rob2)
            rob1 = rob2     # shift the window up one house
            rob2 = newRob
        return rob2  # best total from all the houses