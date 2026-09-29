class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # a consecutive sequence is a sequence of elements in which each element is exactly
        # 1 greater than the previous element

        # elements do not need to be consecutive in the original array 

        res = 0

        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res