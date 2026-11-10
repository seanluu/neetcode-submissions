class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0] # set res to first index in case it's the only one in the array

        l, r = 0, len(nums) - 1 # define left and right pointers

        # use binary search since we want to find a particular number (min) in the sorted array
        while l <= r:
            if nums[l] < nums[r]: # everything is sorted already so we're happy with this order
                res = min(res, nums[l]) # since nums[l] is the minimum of our whole array
                break

            mid = l + ((r - l) // 2) # midpoint of the current range
            res = min(res, nums[mid]) # mid might be the min, save it now since we might move past it

            if nums[mid] >= nums[l]: # mid is in the big piece, min is to the right (so we increment our left pointer to get closer)
                l += 1 # 
            else: # mid is in the small piece, so our min must be to the left (so we decrement our right pointer to get closer)
                r -= 1

        return res