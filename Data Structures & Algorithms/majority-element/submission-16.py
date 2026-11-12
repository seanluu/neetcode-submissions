class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = 0 # final majority element

        maxCount = 0 # curr max frequency

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if maxCount < count[num]:
                res = num
                maxCount = count[num]

        return res