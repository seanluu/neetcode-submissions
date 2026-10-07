class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # one = min cost to reach the previous step, two = the step before that
        # both start at 0 since we can start on step 0 or step 1 for free
        one, two = 0, 0

        # start at 2 since steps 0 and 1 are the base cases (free)
        # therefore, we work past 2 since that is now our recursive step
        # end at len(cost) + 1 so we include the top, which is one past the last index
        for i in range(2, len(cost) + 1):
            temp = one
            # come from i - 1 or i - 2, adding the cost of the step we leave,
            # and keep the cheaper option
            one = min(one + cost[i - 1], two + cost[i - 2])
            two = temp  # shift the window up one step

        return one  # min cost to reach the top