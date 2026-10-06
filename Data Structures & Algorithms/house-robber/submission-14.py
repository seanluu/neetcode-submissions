class Solution:
    def rob(self, nums: List[int]) -> int:

        # top down: recursion follows the arrows to the base case for you
        # bottom-up: start the loop at the base case and fill toward the answer

        # top down vs bottom up
        # Skip the house: dfs(i + 1) vs one
        # Rob the house: nums[i] + dfs(i + 2) vs two + nums[i - 1]
        
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return memo[i]

        return dfs(0)