class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
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