class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # base case: if i (path) >= len(nums) 
        # choices: include nums[i] in subset or exclude nums[i] from subset
        # constraints: i cannot go out of bounds when indexing nums[i]
        # backtracking step: pop the last added element to the subset

        res = []
        subset = []

        def dfs(i):  # i = index we're deciding in/out for
            if i >= len(nums):
                # base case + bounds constraint (same condition, does both):
                # no more indices to decide on & i is no longer valid to index with
                res.append(subset.copy())
                return
            
            # choice #1: include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1) # increment in index once we append to our subset
            subset.pop() # backtracking step

            # choice #2: exclude nums[i] from the subset
            dfs(i + 1) # increment in index, despite not doing anything (excluding nums[i])
        dfs(0) # start at origin
    
        return res