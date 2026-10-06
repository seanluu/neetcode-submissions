class Solution:
    def climbStairs(self, n: int) -> int:
        # can take 1 or 2 steps, so ways(i) = ways(i-1) + ways(i-2)
        # dp[i] = number of ways to reach step i

        dp = [0] * (n + 1)  # one slot for each step, 0 (ground) through n
        dp[0] = 1           # one way to be on the ground: don't move
        dp[1] = 1           # one way to reach step 1: a single 1-step

        for i in range(2, n + 1):         # fill in each step from the bottom up
            dp[i] = dp[i - 1] + dp[i - 2] # came from 1 step below or 2 steps below

        return dp[n]  # ways to reach the top