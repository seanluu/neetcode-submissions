class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # return the k closest points to the origin (0, 0)
        # tells us that we care about the x, y coords in points

        # since we want k closest, therefore it makes sense to use a heap

        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        res = []

        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res