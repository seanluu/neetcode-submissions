class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = {}

        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            if cnt > (len(nums) // 3):
                res.append(num)

        return res