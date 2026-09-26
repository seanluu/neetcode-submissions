class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp -> use smaller subproblems for bigger problems to solve it

        # can climb with either 1 or 2 steps at a time

        # input: n = 2
        # output: 2

        # with 1 + 1 = 2, we have to rely on the first step in our actual answer
        # first step + second step to get 2 steps total, otherwise it doesnt work
        # either 2 single steps, or 1 double step 

        # input: n = 3
        # output: 3

        # with 1 + 1 + 1 = 3, takes 3 single steps on top of each other
        # with 1 + 2 = 3, takes 1 single step, followed by a double step
        # with 2 + 1 = 3, takes 1 double step, followed by a single step

        # try using a decision tree

        # n = 5, solve recursively 
        # if we overshoot with 6 > 5, then we return 0 (since that is not a valid way)
        # 8 different ways, 
        # 5 ways for the 1 case
        # 3 ways for the 2 case 

        # uses 2^n, so we should use memoization to reduce computation again
        # we use dfs on the 1 case, then use it for the 2 case to elim repeated work

        # so only solving one subproblem gives us O(n) time
        # cache = memoization

        # bottom up memoization:
        # 5 -> 4 -> 3 -> 2 -> 1

        # 4 depends on 5, 3 depends on 4, 2 depends on 3, 1 depends on 2

        # 8 5 3 2 1 1 

        # 1 = 1
        # 1 + 1 = 2
        # 1 + 2 = 3
        # 2 + 3 = 5
        # 5 + 3 = 8

        # bottom up recursion

        one, two = 1, 1 
        # one -> number of ways to reach the current step
        # two -> number of ways to reach the previous step
        # essentially, this is just dp[i] = dp[i-1] + dp[i-2] but optimized

        for i in range(n - 1): # runs the recurrence enough times to reach step n and advance DP window forward
            temp = one # temporarily store the previous step's count
            one = one + two # current step = ways from previous step + ways from step before that
            two = temp # shift the previous step forward for the next iteration

        return one # 'one' now holds the total ways to reach step n
        # return the number of ways to reach the top step

        # time complexity: O(n)
        # loop through every number n-1 times -> O(n)

        # space complexity: O(1)
        # only two variables are used so no extra array is needed







