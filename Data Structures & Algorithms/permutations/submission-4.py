class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # if we have nothing, we return an empty list by default
        if len(nums) == 0:
            return [[]]

        # otherwise, we'll skip the first element and permute through the array of nums
        perms = self.permute(nums[1:])
        res = []

        # iterate through each permutation
        for p in perms:
            for i in range(len(p) + 1): 
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res