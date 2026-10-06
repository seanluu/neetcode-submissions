class Solution:
    def climbStairs(self, n: int) -> int:
        # can take 1 or 2 steps, so ways(k) = ways(k-1) + ways(k-2)
        # only need the last two values, so use two variables instead of a DP array

        one, two = 1, 1
        # one = ways to reach the current step (starts at step 1)
        # two = ways to reach the step before it (starts at step 0, the ground)

        for i in range(n - 1):  # one starts at step 1, so n - 1 moves gets it to step n
            temp = one          # save current before overwriting it
            one = one + two     # ways(next) = ways(current) + ways(previous)
            two = temp          # old current becomes the new previous
        return one