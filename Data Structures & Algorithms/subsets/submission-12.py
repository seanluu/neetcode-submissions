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
        
        # Base case: when path length >= len(nums)

        # Choices: include nums[i] in subset or exclude nums[i] in the subset

        # Constraints: i cannot go out of bounds

        # Backtracking step: pop to remove the last added element

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice #1: include nums[i] in subset
            subset.append(nums[i]) 
            dfs(i + 1)
            subset.pop() # backtracking step

            # choice #2: exclude nums[i] in subset
            dfs(i + 1)

        dfs(0) # start at origin
    
        return res # return final array of all valid subsets