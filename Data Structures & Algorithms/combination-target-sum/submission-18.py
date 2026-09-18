class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # base case: if the total == target number, then we're satisfied
        # choices: include nums[i] in our combination (single or multiple times) or exclude it 
        # constraints: total cannot go over target and i cannot go out of bounds when working with nums[i]
        # backtracking step: pop the last added number
        
        res = []

        # index, current path, total sum
        def dfs(i, curr, total):
            if total == target: # base case
                res.append(curr.copy())
                return

            # constraints
            if total > target or i >= len(nums):
                return

            # choice #1: include nums[i] in our combination sum
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # choice #2: exclude nums[i] from our combination sum
            dfs(i + 1, curr, total)

        # start at origin for all parameters
        dfs(0, [], 0)

        return res # return final array of all combination sums