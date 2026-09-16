class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        # iterate through index and val
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # choose first element for triplet
                continue
            
            # skip first element for triplet since we don't want dupes
            l, r = i + 1, len(nums) - 1 

            while l < r:
                threeSum = a + nums[l] + nums[r] # total of triplets should add up to 0
                if threeSum > 0: # too big, decrement
                    r -= 1
                elif threeSum < 0: # too small, increment
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) # otherwise, we found a valid triplet
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # check 2nd and 3rd element being distinct
                        l += 1 # slide left pointer forward
        return res