class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        res = 0

        l, r = 0, len(nums) - 1

        while l <= r: # binary search
            mid = l + ((r - l) // 2) # calculate midpoint
            if nums[mid] > target: # too big, decrement until target found
                r -= 1
            elif nums[mid] < target: # too small, increment until target found
                l += 1
            else:
                return mid # found target
        return -1 # couldn't find target number at all

        # time complexity: O(n)
        # iterate through each num once

        # space complexity: O(1)
        # no crazy data structures used here