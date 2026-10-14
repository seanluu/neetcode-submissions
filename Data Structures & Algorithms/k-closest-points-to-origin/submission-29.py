class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        minHeap = [] # since we want closest points to origin

        # iterate through each coord
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        # while we have k points to add to the heap
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y]) # only care about the points, not the dist
            k -= 1 # decrement k since we figured it out by adding a pair

        return res