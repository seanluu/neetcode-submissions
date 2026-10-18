class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # remove all occurrences of val in nums in-place

        # left pointer
        i = 0

        # right pointer
        for j in range(len(nums)):
            if nums[j] != val: # if our rightmost element doesn't match the value
                nums[i] = nums[j] # we reassign the leftmost element to the rightmost element
                i += 1 # slide our left pointer forward
        return i
