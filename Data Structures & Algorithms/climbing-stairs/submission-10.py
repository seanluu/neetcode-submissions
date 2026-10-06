class Solution:
    def climbStairs(self, n: int) -> int:
        # state:      ways(i) = number of ways to reach step i
        # recurrence: ways(i) = ways(i-1) + ways(i-2)
        #             (last move was a 1-step from i-1 or a 2-step from i-2)

        # ---- optimized: O(1) space ----
        # each step only needs the previous two, so keep two variables
        # instead of a whole array

        one, two = 1, 1
        # base cases:
        # one = ways(1) = 1  (current step)
        # two = ways(0) = 1  (step before it, the ground)

        # order: walk up from step 1 to step n, one step per iteration
        # one starts at step 1, so n - 1 iterations gets it to step n
        for _ in range(n - 1):
            temp = one        # save ways(current) before overwriting it
            one = one + two   # ways(next) = ways(current) + ways(previous)
            two = temp        # old current becomes the new previous

        # answer: one now holds ways(n)
        return one