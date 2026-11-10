class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort to get rid of deduplicates
        nums.sort()
        
        res = []

        # iterate through each index and value
        for i, a in enumerate(nums):
            # skip reusing the first triplet number
            if i > 0 and a == nums[i - 1]: # if we still have indexes to iterate through + our value is equal to the value of the prev index
                continue

            l, r = i + 1, len(nums) - 1 # use two pointers

            while l < r:
                threeSum = a + nums[l] + nums[r] # calculate threeSum
                if threeSum > 0:
                    r -= 1 # too big, decrement to find a better index with a value that will get us to 0
                elif threeSum < 0:
                    l += 1 # too small, increment to find a better index with a value that will get us to 0
                else:
                    res.append([a, nums[l], nums[r]]) # otherwise, we found a valid triplet
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # avoid reusing the second triplet number
                        l += 1

        return res