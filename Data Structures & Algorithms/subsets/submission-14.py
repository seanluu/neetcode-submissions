class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # if base_case condition:
        #     results.append(copy_of_solution)
        #     return

        # for choice in choices:
        #     if violates_constraints:
        #         continue

        #     make_choice
        #     backtrack(updated_params)
        #     undo_choice

        # base case: when path length >= len(nums)
        # constraints: include nums[i] in the subset, or we exclude nums[i] because it isn't part of a subset
        # choices: i cannot go out of bounds
        # backtracking step: pop to remove the previously / last added element

        res = [] # final result array
        subset = [] # each subset has its own array within the results, so it must be created

        # we use i only because we're given an array nums of unique integers
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice #1: include nums[i] in subset
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # choice #2: exclude nums[i] in subset
            dfs(i + 1)
        
        dfs(0) # start at index 0

        return res