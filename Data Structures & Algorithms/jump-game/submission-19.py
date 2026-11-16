class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # work backwards: the goal starts as the last index, and we look for earlier
        # indexes that can reach it
        goal = len(nums) - 1

        # start at the 2nd to last index, since the last index is the goal itself and needs no check
        for i in range(len(nums) - 2, -1, -1): # start, stop, step
            # i + nums[i] is the farthest index we can jump to from i
            if i + nums[i] >= goal:
                goal = i # i can reach the goal, so i is now the new goal

        # if the goal moved all the way back to index 0, we can reach the end from the start
        return goal == 0