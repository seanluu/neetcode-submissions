class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # base case: if i >= len(nums)
        # choices: include nums[i] or exclude nums[i] from our subset
        # constraints: i cannot go out of bounds
        # backtracking step: pop the last added element to curr

        # no duplicate subsets are allowed...

        nums.sort() # sort to get rid of deduplicates

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
            