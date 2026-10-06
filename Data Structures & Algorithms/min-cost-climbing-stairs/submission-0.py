class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of leaving step i, then we can go up 1 or 2
        # we can start on step 0 or 1 for free, and the top is past the last index
        # min cost to reach step i = min(reach i-1 + leave i-1, reach i-2 + leave i-2)

        one, two = 0, 0
        # one = min cost to reach the previous step
        # two = min cost to reach the step before that
        # both start at 0 since starting on step 0 or 1 is free

        # compute steps 2 through n, where step n (len(cost)) is the top
        for i in range(2, len(cost) + 1):
            temp = one
            # came from 1 below or 2 below, paying the cost of the step we leave
            one = min(one + cost[i - 1], two + cost[i - 2])

            # ^^^
            # cheapest to reach i = min(
            #     cheapest to reach i-1  +  toll to leave i-1,
            #     cheapest to reach i-2  +  toll to leave i-2
            # )

            two = temp  # shift the window up one step

        return one  # min cost to reach the top