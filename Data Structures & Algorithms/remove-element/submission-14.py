class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Input: nums = [3,2,2,3], val = 3
        # Output: k = 2, nums = [2,2,_,_]

        # we want to remove all 3s (since val = 3);
        # j reads each num, and if nums[j] isn't 3 we keep it by writing it to nums[i]

        # j reads every num, i is where the next kept num gets written;
        # skip anything equal to val, copy everything else to the front
        i = 0

        # iterate through each num in nums
        for j in range(len(nums)): 
            if nums[j] != val: # this num isn't val, so we keep the current value we have at this index
                nums[i] = nums[j] # write it into the next open spot (anything at i was already read, safe to overwrite)
                i += 1 # move the write spot forward
        return i