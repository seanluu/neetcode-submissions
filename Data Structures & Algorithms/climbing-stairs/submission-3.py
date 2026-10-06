class Solution:
    def climbStairs(self, n: int) -> int:
        
        # either 1 or 2 steps at a time

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one