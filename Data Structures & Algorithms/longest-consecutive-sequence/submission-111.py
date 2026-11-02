class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # length of the longest consecutive seq of elements

        # exactly 1 greater than the prev element

        res = 0
        
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                res = max(res, length)

        return res