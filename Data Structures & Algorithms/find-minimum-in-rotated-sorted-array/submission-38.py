class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        res = nums[0] # if we have only one element, obviously we want to return that first

        while l <= r: # binary search applies here since we want to find the min in the sorted array explicitly
            if nums[l] < nums[r]:
                res = max(res, nums[l])
                break

            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l += 1
            else:
                r -= 1
        
        return res
