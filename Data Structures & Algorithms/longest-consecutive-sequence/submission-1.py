class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) # hashset
        # to quickly check if we have an element exactly 1 greater
        res = 0
        
        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                    res = max(res, length)
        return res