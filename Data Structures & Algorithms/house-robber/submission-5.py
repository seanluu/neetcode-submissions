class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1] * len(nums)  # -1 means not computed yet

        def dfs(i):
            # base case: if we pass the last house then there isn't anything to rob
            # (i + 2 can jump past the end, so this catches it before we index nums)
            if i >= len(nums):
                return 0

            # already computed, reuse it
            if memo[i] != -1:
                return memo[i]

            # option 1: rob house i, skip the next adjacent house, so go to i + 2
            # option 2: skip house i, so now we can rob the next adjacent house (i + 1)
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return memo[i]

        return dfs(0)  # start at the first house