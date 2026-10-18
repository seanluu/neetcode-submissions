class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0  # write pointer: next open slot for a kept element

        for j in range(len(nums)):  # read pointer: scans every element
            # if the current element doesn't equal val, keep it
            if nums[j] != val:
                nums[i] = nums[j]  # write the kept value into the next open slot at the front
                i += 1             # move the write pointer forward
        return i  # number of kept elements

        # tc: O(n), one pass through nums
        # sc: O(1), done in place