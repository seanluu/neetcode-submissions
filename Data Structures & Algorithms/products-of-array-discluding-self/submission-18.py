class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        prefix = 1 # everything before me

        # iterate through each num once
        # ascending order
        for i in range(len(nums)):
            res[i] = prefix # set res[i] to 1
            prefix *= nums[i] # multiply + add by the array of nums at the current index

        postfix = 1 # everything after me

        # descending order, since 
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix # multiply + add prefix to the results as well, since everything after should also be included
            postfix *= nums[i]

        return res


