class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # consecutive seq = each element is exactly 1 greater than the previous
        # elements don't have to be next to each other in the original array

        # key idea: a number is the START of a sequence if num - 1 isn't in the set,
        # so we only count upward from starts, and each sequence is counted once

        res = 0  # longest sequence found so far

        numSet = set(nums)  # O(1) lookups for whether a number exists

        # loop over the set so duplicates don't make us recount the same sequence
        for num in numSet:
            # only start counting if num is the start of a sequence
            if num - 1 not in numSet:
                length = 0
                # count upward while the next number exists
                while num + length in numSet:
                    length += 1
                res = max(res, length)  # keep the longest

        return res

        # time: O(n), each number is visited at most twice
        # (once in the for loop, once while counting up from its start)
        # space: O(n) for the set