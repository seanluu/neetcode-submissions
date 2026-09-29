class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # sorted in ascending order -> binary search
        
        l, r = 0, len(nums) - 1 # use two pointers since we want to search first and last index, then work towards middle 

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1