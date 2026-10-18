class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # frequency matters here, so hashmap works
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # bucket sort: freq[i] holds every number that appears exactly i times
        # size len(nums) + 1 since a number can appear up to len(nums) times
        freq = [[] for _ in range(len(nums) + 1)]

        # put each number into the bucket for its count
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        # go from highest count to lowest (stop at 1, since bucket 0 is empty)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:        # every number with count i
                res.append(num)
                if len(res) == k:      # stop once we have the k we want
                    return res

        return res

        # tc: O(n), counting + filling buckets + one pass over buckets
        # sc: O(n), hashmap + buckets