class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = [] 
        
        # keep track of frequency
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # iterate through num, and the frequency of said number
        for num, cnt in count.items():
            if cnt > (len(nums) // 3): # if element appears more than n/3 times, add it to the results array
                res.append(num)

        return res
