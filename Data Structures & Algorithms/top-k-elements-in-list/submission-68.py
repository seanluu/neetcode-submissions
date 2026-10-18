class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        freq = [ [] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)  # put each number into the bucket matching its count

        res = []

        # go from highest count to lowest (work in descending order)
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]: # iterate through each number in the list of numbers that appear exactly i times
                res.append(num) # add each number respectively to the res array
                if len(res) == k: # once we have the exact number of k freq elements
                    return res # return the array since we don't want any more

        return res # return final array