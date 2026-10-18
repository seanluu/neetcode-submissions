class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # find all elements that appear more than n/3 times
        
        # Input: nums = [5,2,3,2,2,2,2,5,5,5]
        # Output: [2,5]

        # size of n = 10
        # since 2 appears 5 times
        # and 5 appears 4 times
        # and 10 // 3 = 3, therefore we add 2 and 5 to our res array

        count = {} # use a hashmap to keep track of frequency

        # track frequency for each num in our array
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        res = []

        # loop over every distinct number and its count;
        # checking count[num] outside a loop would only test the last num
        for num, cnt in count.items():
            if cnt > (len(nums) // 3):
                res.append(num)

        return res

        # tc: O(n), since we iterate through each num once
        # sc: O(n) for the hashmap