class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # use two pointers since it is sorted in non-decreasing order
        
        l, r = 0, len(numbers) - 1

        while l < r:
            bestSum = numbers[l] + numbers[r] # since we want to sum to a given target number
            if bestSum > target: # too big, decrement
                r -= 1
            elif bestSum < target: # too small, increment
                l += 1
            else:
                return [l + 1, r + 1]