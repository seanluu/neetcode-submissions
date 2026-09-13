class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # use two pointers here since we have a target sum
        l, r = 0, len(numbers) - 1

        while l < r:
            bestSum = numbers[l] + numbers[r] # return indices of these two nums given
            # that they add up to a given target
            if bestSum > target: # too big, decrement by 1
                r -= 1
            elif bestSum < target: # too small, increment by 1
                l += 1
            else:
                return [l + 1, r + 1] # otherwise, target is found
                # we use +1 for both since by description, it should be 1-indexed 

        # time complexity: O(n)
        # iterate through each number at least once

        # space complexity: O(1)
        # no crazy data structures used here