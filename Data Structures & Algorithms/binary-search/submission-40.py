class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 # first and last index

        res = 0 # since we want to return an integer

        while l <= r: # use <= for binary search since we're looking for a very specific number
            mid = l + ((r - l) // 2) # calculate midpoint so we know to slice the array in half
            if nums[mid] > target: 
                r = mid - 1 # too big, decrement window of search
            elif nums[mid] < target:
                l = mid + 1 # too small, increment window of search
            else:
                return mid # return final specific number if we've found it
        return -1 # otherwise, return -1 since we never found the number we actually wanted

        # time complexity: O(n)
        # iterate through each num in nums exactly once

        # space complexity: O(1)
        # no crazy data structures used here