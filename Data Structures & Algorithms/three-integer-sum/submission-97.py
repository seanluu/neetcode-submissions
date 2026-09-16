class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # order in numerical order
        # to avoid repeating permutations

        res = [] # return an actual array

        for i, a in enumerate(nums): # iterate through both index and vals
            
            # choose first element for triplet
            if i > 0 and a == nums[i - 1]:
                continue
            
            # skip first num part of triplet
            l, r = i + 1, len(nums) - 1

            # use two pointers
            while l < r:
                threeSum = a + nums[l] + nums[r] # add all elements part of triplet together
                if threeSum < 0: 
                    l += 1 # threeSum is too small, move pointer forward
                    # to find a better element for our triplet to add up to 0
                elif threeSum > 0:
                    r -= 1 # threeSum is too small, decrement pointer 
                    # # to find a better element for our triplet to add up to 0
                else:
                    res.append([a, nums[l], nums[r]]) # otherwise, we found a valid triplet
                    l += 1 # slide left pointer forward
                    r -= 1 # slide right pointer backwards
                    while l < r and nums[l] == nums[l - 1]: # make sure 2nd and 3rd element are distinct
                        l += 1 # slide left pointer forward
        return res # return final array filled with all valid distinct triplets

        # time complexity: O(n^2)
        # sort is O(n log n), outer loop is O(n), and for each outer iteration
        # the two-pointer sweep is O(n) in the worst case -> O(n^2) dominates

        # space complexity: O(log n) to O(n)
        # excluding the output array, this comes from the sort's internal space
        # (Timsort uses O(n) worst-case, though often closer to O(log n))
