class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # start at the end, since it will quickly help us rule out jumps that can't reach the end
        goal = len(nums) - 1

        # start in descending order to find out quicker
        # if it's possible to reach last index starting from 0

        # start at the 2nd to last index, since the last index is the goal itself and needs no check
        for i in range(len(nums) - 2, -1, -1): # start, stop, step
            if i + nums[i] >= goal: # if curr index and val at the curr index > the goal
                goal = i # set goal to be in the index
            
        return goal == 0 # goal moved all the way back to the start