class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # max heap
        heap = [-n for n in nums]

        heapq.heapify(heap)

        # iterate through each k once
        for i in range(k):
            res = heapq.heappop(heap)

        return -res # return as a negative since we're using a max heap
        # -(-res) should cancel out and become a positive