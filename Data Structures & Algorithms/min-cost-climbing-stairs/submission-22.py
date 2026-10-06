class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # bottom-up dp
        # one = min cost to reach the previous step, two = the step before that
        # both start at 0 since we can start on step 0 or 1 for free

        one, two = 0, 0

        for i in range(2, len(cost) + 1):
            temp = one
            # cheapest way to reach step i: either come from i - 1 or i - 2,
            # adding the cost of the step we leave, and keep the smaller one
            one = min(one + cost[i - 1], two + cost[i - 2])
            two = temp  # shift the window up one step

        return one  # min cost to reach the top