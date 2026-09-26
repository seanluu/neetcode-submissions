class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # base case: len(perm) == len(nums), every num placed
        # choices: any unused index, any call — order matters so no "forward only"
        # constraints: pick[i] tracks used, since depth alone can't tell us anymore
        # backtracking step: pop perm AND reset pick[i] = False (two things mutated)
        
        self.res = []
        self.backtrack([], nums, [False] * len(nums)) # start empty, nothing used yet
        return self.res

    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums): # base case: full-length arrangement done
            self.res.append(perm[:]) # copy, perm keeps mutating after this
            return
        for i in range(len(nums)): # choices: every index, every call (no start bound)
            if not pick[i]: # constraint: skip if already placed in this branch
                perm.append(nums[i]) # choice: place nums[i] next
                pick[i] = True # mark it as used for this branch
                self.backtrack(perm, nums, pick) # recurse deeper with this placement locked in
                perm.pop() # backtracking step where we pop the recently added number
                pick[i] = False # free index i for other branches
        