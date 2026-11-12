class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = 0

        maxCount = 0

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if maxCount < count[num]: # if old majority < current count of our num
                res = num # make it our new leader / majority
                maxCount = count[num] # reassign the maxCount to use the frequency/count of our new leader
            
        return res