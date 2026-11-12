class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            # already in sorted order, so we can just return the left pointer since that's the min
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # calculate midpoint of our array
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid]) 

            # not in sorted order
            if nums[mid] >= nums[l]: # mid is in the big piece
                l = mid + 1 # min is in the right half, jump past mid
            else: # mid is in the small piece
                r = mid - 1 # min is at mid or to the left, jump left (mid already saved)
 
        return res