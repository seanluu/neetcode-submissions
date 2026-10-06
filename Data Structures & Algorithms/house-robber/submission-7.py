class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # start at 0 for both since no houses means no money
        one, two = 0, 0

        # each iteration adds house i - 1 (the newest house)
        for i in range(1, len(nums) + 1):
            temp = one
            # option 1: don't rob the newest house, so we keep the best so far (one)
            # option 2: rob nums[i - 1], so we can't have robbed the previous house,
            #           and we add it to the best from two houses back (two)
            one = max(one, two + nums[i - 1])
            two = temp
        return one