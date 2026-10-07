class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # two pointers at both ends, works because numbers is sorted:
        # moving r left makes the sum smaller, moving l right makes it bigger
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]  # sum of the current pair

            if curSum > target:    # too big, move r left to get a smaller sum
                r -= 1
            elif curSum < target:  # too small, move l right to get a bigger sum
                l += 1
            else:
                return [l + 1, r + 1]  # found it, + 1 since the answer is 1-indexed

        # time: O(n), each pointer moves at most n times total
        # space: O(1), just two pointers