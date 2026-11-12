class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        freq = [ [] for i in range(len(nums) + 1)] # create buckets for each num in nums

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, -1, -1): # go in descending order for frequency
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res