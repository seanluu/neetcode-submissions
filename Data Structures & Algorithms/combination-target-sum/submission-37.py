class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case: if total == target, stop
        # constraints: i cannot go out of bounds
        # choices: include nums[i] in our comb sum, or exclude it
        # backtracking step: pop the last added element to the 

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