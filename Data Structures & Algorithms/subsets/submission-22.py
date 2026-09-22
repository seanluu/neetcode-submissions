class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # we know this is backtracking because we want to return all possible subsets of nums
        # so we're constantly trying and retrying diff results

        # base case: if 
        # choices: either include nums[i] or exclude nums[i]
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice #1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # choice #2: exclude nums[i]
            dfs(i + 1)

        dfs(0)

        return res

            