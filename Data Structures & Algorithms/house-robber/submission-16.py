class Solution:
    def rob(self, nums: List[int]) -> int:

        # bottom-up dp
        
        # start at 0 for both since no houses means no money
        one, two = 0, 0

        # each iteration adds house i - 1 (the newest house)
        for i in range(1, len(nums) + 1):
            temp = one
            # option 1: skip the newest house, so the total is same as the best up to the previous house
            # option 2: rob the newest house, so you have to build on a total that ends 
            #           before the previous house, which is two
            one = max(one, two + nums[i - 1])
            two = temp
        return one