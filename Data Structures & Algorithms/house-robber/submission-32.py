class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # one = max money robbed up to the previous house
        # two = max money robbed up to the house before that
        one, two = 0, 0

        # i is 1-indexed, so nums[i - 1] is the current house (every house is visited)
        for i in range(1, len(nums) + 1):
            temp = one
            # choice 1: skip the current house, keep the best total through the previous house (one)
            # choice 2: rob the current house, add it to the best total from two houses back (two)
            one = max(one, two + nums[i - 1])
            # shift the window forward: the old "previous" becomes "two houses back"
            two = temp
        return one