class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # consecutive seq is a seq of elements in which each element is exactly 1
        # greater than the previous element; the elements don't have to be consecutive
        # in the original array

        numSet = set(nums)

        res = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res