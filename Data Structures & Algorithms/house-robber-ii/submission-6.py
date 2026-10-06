class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # return the first house if there is only one house
        if len(nums) == 1:
            return nums[0]
        
        # memo[i][flag], -1 means not computed yet
        memo = [[-1] * 2 for i in range(len(nums))]

        def dfs(i, flag):
            # stop if index is out of bounds, or if we reach the last house
            # while the first house was allowed (first and last house are neighbors)
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            # if subproblem is already completed, just return it outright
            if memo[i][flag] != -1:
                return memo[i][flag]

            # option 1: rob house i, skip its neighbor, and move to i + 2
            # option 2: skip house i and move to i + 1
            memo[i][flag] = max(nums[i] + dfs(i + 2, flag or i == 0), dfs(i + 1, flag))

            return memo[i][flag]

        # start from house 0, first house is allowed, so last house is banned
        # start from house 1, first house is banned, so last house is allowed
        return max(dfs(0, True), dfs(1, False))