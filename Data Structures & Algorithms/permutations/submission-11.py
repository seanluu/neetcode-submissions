class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # base case: idx == len(nums), every position filled, nums is one full permutation
        # choices: any element from idx onward can be swapped into position idx
        # constraints: none explicit, the prefix nums[:idx] is used and the loop never looks at it
        # backtracking step: swap back, a swap undoes itself
        
        self.res = []
        self.backtrack(nums, 0) # start by filling position 0

        return self.res
    
    def backtrack(self, nums, idx): # idx = the position we're deciding right now
        if idx == len(nums): # base case: every position is filled, nums is one full permutation
            self.res.append(nums.copy()) # copy, since nums keeps getting swapped after this
            return

        # choices: any element from idx onward (the "remaining" part) can go into position idx
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx] # choice: swap nums[i] into position idx
            self.backtrack(nums, idx + 1)           # recurse: now fill the next position
            nums[idx], nums[i] = nums[i], nums[idx] # backtrack: swap back to undo