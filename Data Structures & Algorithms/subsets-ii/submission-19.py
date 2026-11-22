class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # base case: if i >= len(nums), we have a valid subset
        # choices: include nums[i] or exclude nums[i] from our subset
        # constraints: no duplicate subsets, handled by skipping copies in the exclude branch
        # backtracking step: pop the last added element to our curr path
        
        # sort all numbers to be in numerical order
        # helps us avoid duplicate subsets
        nums.sort()

        res = []

        def dfs(i, curr):
            # base case: valid subset
            if i >= len(nums):
                res.append(curr.copy())
                return

            # choice 1: include nums[i] from our subset
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            # choice #2: exclude nums[i] from our subset
            # bounds check for i + 1 first, then check if val of curr element == val of the next element. if it is, then we have a duplicate, so we increment i by 1 to avoid dupes
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr)

        dfs(0, []) # start at origin for both params

        return res