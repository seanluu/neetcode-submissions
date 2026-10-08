class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # use a hashmap for frequency of elements

        # iterate through each num in array once
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # use bucket sort since we'll want to keep track of frequency for each element so far
        freq = [ [] for i in range(len(nums) + 1)] 

        # put each number into the bucket for its count
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        # iterate through in descending order since we care about the MOST frequent elements
        for i in range(len(freq) - 1, 0, -1): # (start, stop, step), stop at 0 since every number appears at least once
            for num in freq[i]: # every number that appears i times
                res.append(num)
                if len(res) == k: # found k numbers, done
                    return res