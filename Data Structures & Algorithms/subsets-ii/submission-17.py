class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # base case: if i >= len(nums), stop
        # choices: include nums[i] in our subset or exclude it
        # constraints: i cannot go out of bounds; when excluding nums[i], also skip its
        # duplicates so we don't build the same subset twice (needs nums sorted first)
        # backtracking step: pop the last added element to the curr path

        nums.sort() # group equal values together so the skip-ahead below can detect them

        res = []

        def dfs(i, curr):
            if i >= len(nums): # base case
                res.append(curr.copy())
                return

            # choice #1: include nums[i]
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop() # backtracking step

            # choice #2: exclude nums[i], and skip all its duplicates too so we don't
            # rebuild a subset we already made by including this value
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr) 

        dfs(0, []) # start at origin for all parameters

        return res