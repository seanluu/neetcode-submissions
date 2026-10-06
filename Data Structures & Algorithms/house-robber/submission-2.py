class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # can't rob two adjacent houses otherwise police will know

        # use -1 as placeholder since we haven't computed dfs(i) for this house yet
        memo = [-1] * len(nums)

        def dfs(i):
            # base case
            if i >= len(nums):
                return 0 

            # if it is not a placeholder, then we can return the value outright
            if memo[i] != -1:
                return memo[i]

            # option 1: we rob the house and take nums[i] 
            # (the amount of money that the ith house has)
            # rob house i: i + 1 is adjacent and blocked, 
            # so the closest allowed house is i + 2

            # option 2: or skip house i and move to the next
            # skip house i: nothing is blocked, so the next house i + 1 is fair game
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return memo[i]

        return dfs(0)