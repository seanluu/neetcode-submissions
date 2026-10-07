class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # one = most money from the houses so far, 
        # two = the best from one house before that
        # both start at 0 since no houses means no money
        one, two = 0, 0

        # start after 1, since our base cases are at 0
        for i in range(1, len(nums) + 1):
            temp = one
            one = max(one, two + nums[i - 1])
            two = temp
        return one
        