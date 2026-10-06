class Solution:
    def rob(self, nums: List[int]) -> int:

        # if there's only 1 house, return its value
        if len(nums) == 1:
            return nums[0]

        # memo for index (curr house) and flag (whether the first house is allowed,
        # meaning the last house is banned)
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            # stop if index is out of bounds, or if we reach the last house
            # while the first house was allowed (they're neighbors in the circle)
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            # if this subproblem was already computed, return it outright
            if memo[i][flag] != -1:
                return memo[i][flag]

            # option 1: skip house i, move to i + 1
            # option 2: rob house i, skip its neighbor, move to i + 2
            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))

            return memo[i][flag]

        # start from house 0 (first house allowed, so last house banned)
        # start from house 1 (first house skipped, so last house allowed)
        return max(dfs(0, True), dfs(1, False))