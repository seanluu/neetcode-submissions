class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # base case: idx == len(nums), so every position is filled and nums is one full permutation
        # choices: for each remaining number, swap it into the current spot (idx)
        # constraints: each number used once, handled by only choosing from idx onward
        # backtracking step: swap back to undo the choice before trying the next number
        
        self.res = []
        self.backtrack(nums, 0)

        return self.res

    # keep track of nums array, and the index
    def backtrack(self, nums, idx):
        # base case: every position is filled and nums is one full permutation
        if idx == len(nums):
            self.res.append(nums.copy())
            return

        # choice: for each remaining number, swap it into the current spot (idx)
        # idx = the spot we're filling (stays fixed in this call)
        # i   = the candidate number we're trying in that spot (moves each loop)
        for i in range(idx, len(nums)):            # try each remaining number (idx to end)
            nums[idx], nums[i] = nums[i], nums[idx]  # place nums[i] in spot idx
            self.backtrack(nums, idx + 1)            # fill the next spot
            nums[idx], nums[i] = nums[i], nums[idx]  # swap back to undo before trying the next number