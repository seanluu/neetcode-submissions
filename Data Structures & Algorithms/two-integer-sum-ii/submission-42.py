class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointers
        l, r = 0, len(numbers) - 1

        while l < r:
            bestSum = numbers[l] + numbers[r] # calculate the bestSum we can
            if bestSum > target: # too big for target, decrement to find a sum closer to target
                r -= 1
            elif bestSum < target: # too small for target, increment to find a sum closer to target
                l += 1
            else:
                return [l + 1, r + 1] # 1-indexed so we use +1 for both

        # time complexity: O(n)
        # iterate through each num in numbers once

        # space complexity: O(1)
        # no crazy data structures