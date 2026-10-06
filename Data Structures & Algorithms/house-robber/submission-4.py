class Solution:
    def rob(self, nums: List[int]) -> int:

        # can't rob two adjacent houses
        # dfs(i) = most money we can get from house i to the end

        memo = [-1] * len(nums)  # -1 means not computed yet (money is never negative)

        def dfs(i):
            # base case: past the last house, nothing left to rob
            if i >= len(nums):
                return 0

            # already computed, reuse it
            if memo[i] != -1:
                return memo[i]

            # option 1: rob house i, so skip its neighbor and go to i + 2
            # option 2: skip house i, so the next house i + 1 is still fair game
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return memo[i]

        return dfs(0)  # start at the first house