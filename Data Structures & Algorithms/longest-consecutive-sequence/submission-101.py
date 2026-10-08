class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # length of the longest consecutive sequence of elements

        # consecutive seq is a seq of elements in which each element is exactly
        # 1 greater than the previous element

        # elements do not have to be consecutive in the original array

        # Input: nums = [2,20,4,10,3,4,5]
        # Output: 4

        # since we can do 2, 3, 4, 5
        # a way we can handle this is by checking if the start of the sequence is
        # already in the array (using a set)

        numSet = set(nums)

        res = 0

        # iterate through each num in the array of nums
        for num in nums:
            if num - 1 not in numSet: # if start of consec isn't in numSet
                length = 0 # then we know that it is not a consecutive
                while num + length in numSet: # we have a consecutive, keep incrementing
                    length += 1 
                res = max(res, length)
        return res