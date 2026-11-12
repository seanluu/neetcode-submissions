class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = 0

        maxCount = 0

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            if cnt > (len(nums) // 2):
                return num