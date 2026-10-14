class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # count only when we find the beginning of a consecutive sequence

        res = 0
        
        numSet = set(nums)

        for num in nums:
            # a number is the start of a sequence if num - 1 is not in the set
            # this guarantees each consecutive sequence is counted exactly once
            if num - 1 not in numSet:
                length = 0
                # keep checking if num + 1, num + 2, ... and extend streak as far as possible
                while num + length in numSet:
                    length += 1
                res = max(res, length) # update res with the max length found
        return res # return the longest consec seq