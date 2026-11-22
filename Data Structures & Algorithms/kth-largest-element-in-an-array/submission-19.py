class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # find kth largest in an array
        # therefore we use a max heap

        heap = [-num for num in nums]

        heapq.heapify(heap)

        for i in range(k):
            res = heapq.heappop(heap)

        return -res