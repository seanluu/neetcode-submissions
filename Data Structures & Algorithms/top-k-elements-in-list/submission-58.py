class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # since we want to keep track of most frequent elements
        # it makes sense here to use a hashmap

        for num in nums:
            count[num] = 1 + count.get(num, 0) # increment count if key exists, otherwise we'll start at 0

        # bucket sort since we can just keep track of elements per number
        # freq[i] stores all numbers that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res