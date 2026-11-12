class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0

        for j in range(len(nums)):
            if nums[j] != val: # nums[j] isn't val, so keep it
                nums[i] = nums[j] # copy nums[j] into nums[i], the next open spot at the front
                i += 1 # move the open spot forward
        return i