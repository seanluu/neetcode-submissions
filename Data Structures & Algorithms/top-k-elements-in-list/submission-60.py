class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # since we want to keep track of most frequent elements
        # it makes sense here to use a hashmap

        for num in nums:
            count[num] = 1 + count.get(num, 0) # increment count if key exists, otherwise we'll start at 0

        # bucket sort since we can just keep track of elements per number
        # freq[i] stores all numbers that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]

        # iterate through each number and its frequency
        for num, cnt in count.items():
            freq[cnt].append(num) # place this number into the bucket for its total frequency cnt
            # (runs once per UNIQUE number, not once per occurrence)

        res = []

        # return most frequent elements in descending order (from most to least)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]: # for every number that appears exactly i times
                res.append(num) # we want to add that number to the results array
                if len(res) == k: # once we hit the k number of freq elements
                    return res # no more elements are necessary since it's been fulfilled
                    # so we're free to return the final array of the k most freq elements
        
        # time complexity: O(n)
        # one pass to count frequencies, one pass to bucket them,
        # one pass (bounded by n total elements across all buckets) to collect results
        # no comparison-based sorting used, so no log(n) factor

        # space complexity: O(n)
        # count dict holds up to n unique numbers, freq list has n+1 buckets,
        # and res holds up to k <= n numbers