class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Input: nums = [2,20,4,10,3,4,5]
        # Output: 4

        # a consecutive sequence is a sequence of elements in 
        # which each element is exactly 1 greater than the prev element

        # check 2 < 20, 2 < 4, 2 < 10 all fail
        # 2, 3, 4, 5 works though

        numSet = set(nums) # we can use a hashset to quickly keep track of numbers in O(1) time throughout the array

        res = 0 # output is an integer

        for num in nums:
            if num - 1 not in numSet: # nothing before num, so num is the start of a sequence
                length = 1
                while num + length in numSet: # keep extending while the next number exists
                    length += 1
                res = max(res, length) # take the longest consecutive sequence we've seen so far
        return res

        # tc: O(n), each num is visited once by the for loop and at most once by a while loop
        # sc: O(n), hashset of all nums