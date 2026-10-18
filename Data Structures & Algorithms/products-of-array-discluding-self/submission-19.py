class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)  # will hold prefix * postfix for each index

        prefix = 1  # product of everything before i

        # left to right: build up the product of everything before each index
        for i in range(len(nums)):
            res[i] = prefix      # res[i] = product of everything before i
            prefix *= nums[i]    # include nums[i] for the next index

        postfix = 1  # product of everything after i

        # right to left, so postfix builds up from the end
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix    # before i (already stored) * after i
            postfix *= nums[i]   # include nums[i] for the next index to the left

        return res

        # tc: O(n), two passes
        # sc: O(1) extra (res is the output, doesn't count)