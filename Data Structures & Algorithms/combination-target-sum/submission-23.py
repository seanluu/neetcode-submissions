class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # base case: if the chosen combined nums sum to target
        # choices: either include nums[i] in our combination sum OR exclude nums[i] from it
        # constraints: i cannot go out of bounds; if total exceeds target, stop this branch (return)
        # backtracking step: pop the last added element to the path
        
        res = []

        # index, current path, total
        def dfs(i, curr, total):
            if total == target: # base case: if chosen numbers sum to target, add to the combination sum
                res.append(curr.copy())
                return

            # constraints: i cannot go out of bounds, total cannot be greater than target
            if total > target or i >= len(nums):
                return

            # choice #1: include nums[i] in our combination sum
            curr.append(nums[i])
            dfs(i, curr, total + nums[i]) 
            curr.pop() # backtracking step

            # choice #2: exclude nums[i] in our combination sum
            dfs(i + 1, curr, total) # done considering nums[i] at this level — move to the next candidate
        
        dfs(0, [], 0) # start at origin for all parameters

        return res # return final array of all combination sums made