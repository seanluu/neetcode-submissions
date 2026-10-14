class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case: if target == total, stop here
        # choices: include nums[i] or exclude nums[i] in the comb sum
        # constraints: i cannot be out of bounds and total cannot be greater than the target
        # backtracking step: pop the last added element to the curr path

        res = []

        def dfs(i, curr, total):
            if target == total:
                res.append(curr.copy())
                return

            if total > target or i >= len(nums):
                return

            # choice #1: include nums[i]
            curr.append(nums[i])
            dfs(i, curr, nums[i] + total)
            curr.pop()

            # choice #2: exclude nums[i]
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res
