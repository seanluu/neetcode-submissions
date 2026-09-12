class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        numSet = set(nums) # return the length of the longest consec seq of elements
        # within this array of integers nums specifically

        # iterate through each num in the array nums
        for num in nums:
            if num - 1 not in numSet: # if exactly 1 greater than the prev element isn't present
            # then we know that it isn't a consecutive sequence 
                length = 0 # therefore, we can say that the length is 0
                while num + length in numSet: # must mean it is a consecutive
                    length += 1 # continue incrementing length
                res = max(res, length) # take longest consec seq so far
        return res # return final result

        # time complexity: O(n)
        # iterate through each num at least once

        # space complexity: O(n)
        # numSet stores up to n elements (one copy of each number in nums)