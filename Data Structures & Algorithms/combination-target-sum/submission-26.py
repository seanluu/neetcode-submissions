class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case: stop once chosen numbers sum to target
        # choices: include nums[i] in our combination sum, or exclude it altogether
        # constraints: i cannot go out of bounds, and total cannot be greater than the target
        # backtracking step: pop the last added element to the current path

        res = []

        # index, current path, total of chosen numbers
        def dfs(i, curr, total):
            if total == target: # base case
                res.append(curr.copy())
                return

            # constraints
            if total > target or i >= len(nums):
                return

            # choice #1: include nums[i] in our combination sum
            curr.append(nums[i])
            dfs(i, curr, total + nums[i]) # leave as i for i, since it's possible for us to choose
            # the same number from nums an unlimited number of times
            curr.pop()

            # choice #2: exclude nums[i] from our combination sum
            dfs(i + 1, curr, total)

        dfs(0, [], 0) # start at origin for all parameters

        return res