class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one, two = 0, 0
        # one = min cost to reach the previous step, two = the step before that
        # both 0 since we can start on step 0 or 1 for free
        # (unlike climbing stairs, where it's 1 because there's 1 way to start)

        # start at 2 since steps 0 and 1 are free (base cases)
        # end at len(cost) + 1 so we include the top, which is one past the last index
        for i in range(2, len(cost) + 1):
            temp = one
            one = min(one + cost[i - 1], two + cost[i - 2])
            two = temp
        return one