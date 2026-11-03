class Solution:
    def rob(self, nums: List[int]) -> int:
        
        one, two = 0, 0

        for i in range(1, len(nums) + 1):
            temp = one
            one = max(one, nums[i - 1] + two)
            two = temp
        return one