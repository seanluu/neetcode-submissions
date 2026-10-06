class Solution:
    def climbStairs(self, n: int) -> int:
        
        # only either 1 or 2 steps at a time

        # dp[i] = dp[i - 1] + dp[i - 2]  # last move was a 1-step from i-1 or a 2-step from i-2
        one, two = 1, 1

        # since the base cases already cover steps 0 and 1,
        # we only need to compute steps 2 through n, which is n - 1 values
        for i in range(n - 1):
            temp = one # temporarily store 1 step at a time
            one = one + two # two steps at a time
            two = temp # or one step at a time

        return one