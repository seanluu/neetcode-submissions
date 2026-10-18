class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # we care about most frequent element, so hashmap makes sense

        # Input: nums = [5,5,1,1,1,5,5]
        # Output: 5

        res = 0  # current majority candidate

        maxCount = 0  # highest frequency seen so far

        count = {}

        # take frequency for each element in the array
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            # if num's count beats the best count so far, it's the new leader
            if maxCount < count[num]:
                res = num               # update the candidate
                maxCount = count[num]   # track the highest frequency seen so far

        return res

        # tc: O(n), one pass
        # sc: O(n), hashmap stores counts for up to n distinct values