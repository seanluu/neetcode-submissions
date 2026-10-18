class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Input: nums = [1,2,4,6]
        # Output: [48,24,12,8]

        # works since 
        # 6 * 4 * 2 * 1 = 48
        # 6 * 4 * 1 = 24
        # 6 * 2 * 1 = 12
        # 4 * 2 * 1 = 8

        # prefix sum = "everything before me"
        # postfix sum = "everything after me"

        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


