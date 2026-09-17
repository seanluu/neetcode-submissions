class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # base case: when the path length >= len(nums)
        # choices: include nums[i] in the subset or exclude nums[i] from it
        # constraints: stop once path goes out of bounds
        # backtracking step: pop the last added element

        # if base_case_condition:
            # results.append(copy_of_solution)
            # return

        # for choice in choices:
            # if violates_constraints:
                # continue
            
            # make_choice
            # backtrack(updated_params)
            # undo_choice # backtracking step
        
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums): # base case: 
                res.append(subset.copy()) # save curr subset
                return
            
            # choice #1: include nums[i] in subset
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop() # backtracking step

            # choice #2: exclude nums[i] in subset
            dfs(i + 1)
        
        # start recursion from the first element
        dfs(0)
    
        # return list of all subsets
        return res