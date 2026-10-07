class Solution:
    def rob(self, nums: List[int]) -> int:

        # base case: if we have a single house, return it outright
        if len(nums) == 1:
            return nums[0]

        # memo[i][flag], -1 means not computed yet
        # flag = True means the last house is banned (since the first house might be robbed)
        memo = [[-1] * 2 for i in range(len(nums))]

        def dfs(i, flag):
            # stop if out of bounds, or if we reach the last house while it's banned
            # (first and last are neighbors in the circle)
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            # already computed, reuse it
            if memo[i][flag] != -1:
                return memo[i][flag]

            # option 1: rob house i, skip its neighbor, move to i + 2
            #           (robbing the first house turns the flag on)
            # option 2: skip house i, move to i + 1 (flag stays the same)
            memo[i][flag] = max(nums[i] + dfs(i + 2, flag or i == 0), dfs(i + 1, flag))

            return memo[i][flag]

        # start from house 0 (last house banned) or house 1 (last house allowed)
        return max(dfs(0, True), dfs(1, False))