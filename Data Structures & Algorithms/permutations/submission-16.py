class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0) # start at origin for backtrack

        return self.res

    def backtrack(self, nums, idx):
        if idx == len(nums):
            self.res.append(nums.copy())
            return

        # spot idx is fixed; try each remaining number (idx to end) in that spot
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]  # choose: put nums[i] in spot idx
            self.backtrack(nums, idx + 1)            # explore: fill the next spot
            nums[idx], nums[i] = nums[i], nums[idx]  # backtrack: swap back to undo