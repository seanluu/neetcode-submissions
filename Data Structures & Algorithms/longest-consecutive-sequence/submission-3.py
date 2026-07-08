class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Input: nums = [2,20,4,10,3,4,5]
        # Output: 4

        # 2 < 20 false
        # 20 < 4 false
        # 4 < 10 false
        # 10 < 3 false
        # 3 < 4 true
        # 4 < 5 true

        # since elements don't have to be consecutive, we can get away with
        # saying 2 < 3 < 4 < 5, therefore 4
        
        numSet = set(nums) # hashset is necessary since it lets us
        # quickly check whether we have n + 1, since we do want to check
        # each element is exactly 1 greater than the prev element

        res = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                    res = max(res, length)
        return res

