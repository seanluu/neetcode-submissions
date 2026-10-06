class Solution:
    def climbStairs(self, n: int) -> int:

        # top-down dp (recursion + memo)
        # dfs(i) = number of ways to get from step i to the top

        memo = [-1] * n  # -1 means not computed yet, only need steps 0 to n - 1

        def dfs(i):
            # base case: landed exactly on the top counts as 1 way (True),
            # overshooting counts as 0 ways (False)
            if i >= n:
                return i == n

            # already computed, reuse it
            if memo[i] != -1:
                return memo[i]

            # take 1 step or take 2 steps, and add up the ways from each
            memo[i] = dfs(i + 1) + dfs(i + 2)

            return memo[i]

        return dfs(0)  # start on the ground