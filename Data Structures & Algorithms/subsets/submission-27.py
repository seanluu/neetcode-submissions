class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # base case: if i >= len(nums)
        # choices: either include nums[i] in our subset or exclude it
        # constraints: i cannot go out of bounds 
        # backtracking step: pop the last added element to the current path

        res = []

        subset = [] # since output calls for subsets to use an array

        # index
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # base case
                return

            # choice #1: include nums[i] in our subset
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop() # backtracking step

            # choice #2: exclude nums[i] from our subset
            dfs(i + 1)

        dfs(0)

        return res