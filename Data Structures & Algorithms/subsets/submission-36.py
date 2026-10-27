class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # base case: if i >= len(nums), stop
        # choices: include nums[i] in our subset or exclude it
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element to our curr path

        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            dfs(i + 1, curr)

        dfs(0, [])

        return res