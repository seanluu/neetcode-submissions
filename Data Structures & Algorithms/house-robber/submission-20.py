class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # one = most money from the houses so far, 
        # two = the best from one house before that
        # both start at 0 since no houses means no money
        one, two = 0, 0

        # start at 1, since our base case is at 0
        for i in range(1, len(nums) + 1):
            temp = one
            # option 1: skip the newest house, so keep the best amt of money so far (one)
            # option 2: rob the newest house (nums[i - 1]), so the previous house
            #           is blocked, and we add it to the best from two houses back (two)
            one = max(one, two + nums[i - 1])
            two = temp
        return one
        