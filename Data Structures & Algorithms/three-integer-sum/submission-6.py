class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = [] # since we want to return an array as our final answer

        nums.sort() # sort in numerical order so we can handle dupes first

        for i, a in enumerate(nums): # find index and value
            if a > 0: # one of the indices is a duplicate
                break

            if i > 0 and a == nums[i - 1]: # continue since we know first indice isn't a dupe
                continue
            
            l, r = i + 1, len(nums) - 1 # skip first indice since we selected one already

            while l < r: # while we have two pointers
                threeSum = a + nums[l] + nums[r] # add all 3 nums together in triplet
                if threeSum > 0: # if total is greater than 0, too big
                    r -= 1 # decrement
                elif threeSum < 0: # if total is smaller than 0, too small
                    l += 1 # increment
                else: # otherwise we can safely add to our triplet
                    res.append([a, nums[l], nums[r]]) # add unique triplet
                    l += 1 # move both pointers
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # make sure 2nd and 3rd indice aren't dupes
                        l += 1 # increment pointer to move onto a new number
        return res # return final list of triplets
                