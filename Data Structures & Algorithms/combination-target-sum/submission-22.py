class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case: if i >= len(nums)
        # choices: either include nums[i] or exclude nums[i]
        # constraints: if total is greater than the target or i cannot go out of bounds
        # backtracking step: pop the last added element to the path

        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res

