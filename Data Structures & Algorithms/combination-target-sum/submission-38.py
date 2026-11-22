class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case: 
        # choices: include nums[i] in our comb sum, or exclude it
        # constraints: total cannot be greater than target, i can't go out of bounds
        # backtracking step: pop the last added element to our curr path

        res = []

        def dfs(i, curr, total):
            # if total == target, we have a valid list of unique combs where the chosen numbers sum to our target
            if total == target:
                res.append(curr.copy())
                return

            # constraints: i is out of bounds or our target > target (both not allowed)
            if i >= len(nums) or total > target:
                return

            # choice #1: include nums[i]
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # choice #2: exclude nums[i]
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res

            