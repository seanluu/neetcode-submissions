class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # return length of the longest consec seq of elements that can be formed

        # consec -> seq of elements in which each element is exactly 1 greater
        # than the previous element

        # Input: nums = [2,20,4,10,3,4,5]
        # Output: 4

        # this works because:
        # 2: 1 not in set -> start, count 2,3,4,5 (6 missing) -> length 4
        # 20: 19 not in set -> start, count 20 (21 missing) -> length 1
        # 4: 3 in set -> skip
        # 10: 9 not in set -> start, count 10 (11 missing) -> length 1
        # 3: 2 in set -> skip
        # 5: 4 in set -> skip

        # longest sequence found: [2,3,4,5] -> length 4, matching expected output

        # since we only ever need to check "does this VALUE exist" (never caring
        # about array position), a hashset works great here for O(1) lookups

        res = 0 # output is an integer, so we use this as a baseline

        numSet = set(nums) # convert to a set for O(1) "does this value exist?" lookups

        # iterate through each number in the array
        for num in nums:
            if num - 1 not in numSet: # num-1 missing means num is the START of a sequence
                length = 0 # begin counting the sequence length from here
                while (num + length) in numSet: # check num, then num+1, num+2, ... as length grows
                    length += 1
                res = max(res, length) # track the longest sequence found so far
        return res

        # time complexity: O(n)
        # iterate through each number in the array nums at least once

        # space complexity: O(n)
        # numSet stores up to n elements — one entry per unique number in nums