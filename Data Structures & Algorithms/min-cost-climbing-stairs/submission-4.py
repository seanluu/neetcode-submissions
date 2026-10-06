class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one, two = 0, 0

        # start at 2 since steps 0 and 1 are free (base cases)
        # end at len(cost) + 1 so we include the top, which is one past the last index
        for i in range(2, len(cost) + 1):
            temp = one
            one = min(one + cost[i - 1], two + cost[i - 2])
            two = temp
        return one