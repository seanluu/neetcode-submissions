class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # top-down dp

        # memoization is where we optimize by remembering results once
        # we compute them, that way we can avoid repeated work

        # memo[i] stores the minimum cost to reach the top from step i
        memo = [-1] * len(cost) # grab the last element

        def dfs(i):
            # base case: if i is beyond the last step, we return 0
            if i >= len(cost):
                return 0
            # if memo[i] is already completed, then return it outright
            if memo[i] != -1: 
                return memo[i]
            # otherwise, we calculate it
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        # since we have the option of starting from step 0 or step 1
        # we will choose the min option between the two
        return min(dfs(0), dfs(1))