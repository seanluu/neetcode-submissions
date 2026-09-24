class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # base case: if i >= len(nums)
        # choices: either include nums[i] or exclude nums[i]
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element to the path
        
        res = []

        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            dfs(i + 1)
        
        dfs(0)

        return res
