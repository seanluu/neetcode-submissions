class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # groups duplicates together so we can skip them, and enables two pointers
        
        res = []

        # iterate through each index and value
        for i, a in enumerate(nums):
            # skip reusing the first triplet number
            if i > 0 and a == nums[i - 1]: # same value as the previous a, so we'd only get duplicate triplets
                continue

            l, r = i + 1, len(nums) - 1 # use two pointers

            while l < r:
                threeSum = a + nums[l] + nums[r] # calculate threeSum
                if threeSum > 0:
                    r -= 1 # sum too big; sorted, so moving r left lowers it
                elif threeSum < 0:
                    l += 1 # sum too small; sorted, so moving l right raises it
                else:
                    res.append([a, nums[l], nums[r]]) # otherwise, we found a valid triplet
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # avoid reusing the second triplet number
                        l += 1

        return res

        # tc: O(n^2), sort is O(n log n) once, then n iterations each with an O(n) two-pointer scan;
        # n log n + n^2 = O(n^2)
        # sc: O(1) -> no crazy data structures used rlly