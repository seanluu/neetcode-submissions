class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # sorted in ascending order -> binary search
        
        l, r = 0, len(nums) - 1 # use two pointers since we want to search first and last index, then work towards middle 

        # use <= since we're working with binary search, and we want to find an exact element
        while l <= r:
            mid = l + ((r - l) // 2) # calculate the midpoint
            if nums[mid] > target: # if our current element is larger than our target
                r = mid - 1 # then it's too big, so we decrement until we find an integer that matches our target
            elif nums[mid] < target: # if our current element is smaller than our target
                l = mid + 1 # then it's too small, so we increment until we find an integer that matches our target
            else:
                return mid # target found
        return -1 # otherwise, no target found so we return -1

        # time complexity: O(n)
        # since we iterate through each num in the nums array at least once

        # space complexity: O(1)
        # no crazy data structures used here