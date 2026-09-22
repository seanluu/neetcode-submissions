class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case: if total == target, stop here
        # choices: either include nums[i] in comb sum or exclude nums[i] from it
        # constraints: total cannot exceed target and i cannot go out of bounds
        # backtracking step: pop the last added element

        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(nums):
                return

            # choice #1: include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # choice #2: exclude nums[i]
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res