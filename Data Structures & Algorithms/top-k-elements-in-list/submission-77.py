class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]

        # since 2 and 3 occur the most in the array, we choose them as our output (limit of 2)
        # since k = 2
        
        # return the k most frequent elements within the array

        count = {} # since we care about the frequency

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []

        freq = [ [] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

            

