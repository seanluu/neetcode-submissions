class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # we care about most frequent element, so hashmap makes sense

        # Input: nums = [5,5,1,1,1,5,5]
        # Output: 5

        res = 0

        maxCount = 0
        
        count = {}

        # take frequency for each element in the array
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            # if current max value is worse than the frequency of an element 
            if maxCount < count[num]:
                res = num # reassign the current result to use the current number (so if 5 is the majority element, now that is what we return)
                maxCount = count[num] # reassign maxCount to keep track of the frequency for what we think is the majority element, so if 5 is the majority element, we say maxCount = 4)
            
        return res