class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # base case: if we have a single house, return it outright
        if len(nums) == 1:
            return nums[0]

        # start at 2 since that is the recursive case
        memo = [[-1] * 2 for i in range(len(nums))]

        def dfs(i, flag):
            # if we have a flag and the index matches the last index, then 
            # first and last are neighbors so we want to stop it from being robbed
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            if memo[i][flag] != -1:
                return memo[i][flag]

            # option 1: rob nums[i] and skip the next adj house OR if it would be robbing
            # a circular house, then return the best money so far of the two houses total

            # option 2: skip robbing the house and just return the best money so far
            memo[i][flag] = max(nums[i] + dfs(i + 2, flag or i == 0), dfs(i + 1, flag))

            return memo[i][flag]

        return max(dfs(0, False), dfs(1, True))