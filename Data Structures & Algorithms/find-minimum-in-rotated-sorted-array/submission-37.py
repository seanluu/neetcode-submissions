class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # originally sorted in ascending order 

        # rotated between 1 and n times

        # Input: nums = [3,4,5,6,1,2]
        # Output: 1

        # since 1 is the minimum of the whole array despite being rotated like 4 times

        # since it was originally sorted in ascending order,
        # we can use binary search to find that exact element that is the minimum 

        l, r = 0, len(nums) - 1 # first and last index

        res = nums[0] # return first element by default as base case
        # if nums = [1], then we output = 1

        while l <= r: # use binary search to find min in rotated sorted array
            if nums[l] < nums[r]: # if array is sorted already
                res = min(res, nums[l]) # set res to use leftmost element of nums
                break # already found our min so we break
            
            mid = l + ((r - l) // 2) # calculate midpoint
            res = min(res, nums[mid]) # if mid value happens to be the min, awesome
            
            # otherwise, array isn't sorted so we must find it by binary search
            if nums[mid] >= nums[l]: # midpoint >= leftmost element
                l = mid + 1 # lh is sorted, min in right portion of array
            else:
                r = mid - 1 # rh is sorted, min in left portion of array
        
        return res # return min value of the array

        # time complexity: O(n)
        # iterate through each num once

        # space complexity: O(1)
        # no crazy data structures used here