class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        minHeap = []

        # take x, y coordinates
        for x, y in points:
            dist = (x ** 2) + (y ** 2) # find euclidean distance between two points
            minHeap.append([dist, x, y]) # add dist, x, y to the minHeap then we will heapify it

        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
