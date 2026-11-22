class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = [] # output is an array

        minHeap = [] # since we're trying to find 
        # the poins that are closest to the origin

        # iterate through each coord once
        for x, y in points:
            # sqrt((x1 - x2)^2 + (y1 - y2)^2))
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        while k > 0: # while we have k closest points to handle
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y]) # only care abt returning x, y coords, not the distance
            k -= 1 # decrement the number of points we have to handle

        return res