class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums) # fill every number as 1 by default

        prefix = 1 # product of everything before i / everything before me

        for i in range(len(nums)):
            # assign res[i] the value of our prefix
            res[i] = prefix  # store the product of everything before i in res[i]
            prefix *= nums[i] # prefix is multiplying by the value at the current index of the array nums

        postfix = 1 # product of everything after i / everything after me

        for i in range(len(nums) - 1, -1, -1):
            # res[i] is multiplying by the value of postfix
            res[i] *= postfix  # multiply in the product of everything after i, so res[i] = before * after (we have stuff to combine so thats why we use *= )
            postfix *= nums[i] # postfix is multiplying by the value at the current index of the array nums

        return res
