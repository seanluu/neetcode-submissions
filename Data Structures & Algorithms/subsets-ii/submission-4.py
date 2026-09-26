class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        def dfs(i, curr):
            # every prefix is itself a valid subset (unlike permute, where only
            # full-length paths count) — so append immediately, every call,
            # not just at a base case
            res.append(curr[::])

            for j in range(i, len(nums)):
                # skip duplicate values at this recursion level (only skips
                # repeats AFTER the first occurrence, since j > i, not j > 0)
                if j > i and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j]) # choice: include nums[j] next
                dfs(j + 1, curr) # recurse — j+1 since no reuse allowed
                curr.pop() # backtrack: undo before trying next j

        dfs(0, []) # set to origin

        return res