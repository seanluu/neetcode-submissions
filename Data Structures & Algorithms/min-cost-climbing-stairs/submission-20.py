class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # top-down dp

        # memoization is where we optimize by remembering results once
        # we compute them, that way we can avoid repeated work

        # memo[i] stores the minimum cost to reach the top from step i, including cost[i]
        memo = [-1] * len(cost)  # one slot per step, -1 means not computed yet

        def dfs(i):
            # base case: at or past the top, so there's nothing left to pay
            if i >= len(cost):
                return 0
            # if memo[i] is already computed, then return it outright
            if memo[i] != -1:
                return memo[i]
            # otherwise, pay to leave step i, then take the cheaper of
            # going up 1 or 2 steps from here

            # we do i + 1 and i + 2 since dfs(i) is the cost from step i to the top,
            # so we look at the steps we can move to next, which are closer to the base case
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        # since we have the option of starting from step 0 or step 1
        # we will choose the min option between the two
        return min(dfs(0), dfs(1))