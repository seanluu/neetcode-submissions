class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # base case: if i >= len(nums)
        # choices: either include nums[i] in our subset or exclude it
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element to the curr path
        
        nums.sort()

        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr)
        
        dfs(0, [])

        return res