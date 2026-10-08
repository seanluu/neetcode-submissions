class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # since we want to find the minimum cost, it makes sense that we use
        # dynamic programming since the answer is constantly changing based
        # on the past subproblems we've solved
        
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        
            return memo[i]
        
        return min(dfs(0), dfs(1))