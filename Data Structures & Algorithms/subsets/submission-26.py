class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # base case: if i >= len(nums)
        # choices: either include nums[i] or exclude nums[i] from the subset
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element to the path

        res = []

        subset = []

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice #1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # choice #2: exclude nums[i]
            dfs(i + 1)

        dfs(0) # reset to origin

        return res
