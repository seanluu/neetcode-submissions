class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # base case: i >= len(nums) means we've made a choice for every element, so curr is a full subset 
        # constraints: none, every combination of elements is a valid subset
        # choices: include nums[i] in our subset, or exclude it
        # backtracking step: pop the last added element to our curr path

        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            # choice #1 of including nums[i]
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            # choice #2: exclude nums[i]
            dfs(i + 1, curr)

        # start at origin for both index and curr path
        dfs(0, [])

        return res 