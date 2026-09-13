class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # use two pointers here since we have a target sum
        l, r = 0, len(numbers) - 1

        res = 0

        while l < r:
            bestSum = numbers[l] + numbers[r] # return indices of these two nums given that they add up to a given target
            if bestSum > target:
                r -= 1
            elif bestSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return res