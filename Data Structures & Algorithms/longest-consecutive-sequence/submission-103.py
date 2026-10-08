class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0  # longest sequence found so far

        # we want a hashset, because we want to quickly look up in O(1) whether
        # an element exists already within our array
        numSet = set(nums)

        # loop over the set so duplicates don't make us recount a sequence
        for num in numSet:
            # num - 1 isn't in the set, so num is the start of a sequence
            if num - 1 not in numSet:
                length = 0  # reset the counter before counting up from this start
                # keep counting while the next number exists
                while num + length in numSet:
                    length += 1
                res = max(res, length)  # keep the longest sequence so far
        return res

        # time: O(n), each number is counted at most once while counting up from its start
        # space: O(n) for the set